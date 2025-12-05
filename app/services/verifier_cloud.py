# app/services/verifier_cloud.py
"""
Cloud-compatible verifier using Hugging Face Inference API (FREE)
This replaces Ollama for cloud deployments where local LLM isn't available.
"""
import os
import json
import requests
from app.utils.search import search_web

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
USE_HUGGINGFACE = os.getenv("USE_HUGGINGFACE", "false").lower() == "true"

# Free Hugging Face model for text generation
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

def call_huggingface_api(prompt: str, max_retries=3):
    """
    Call Hugging Face Inference API with retry logic.
    """
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 500,
            "temperature": 0.3,
            "return_full_text": False
        }
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 503:
                # Model is loading, wait and retry
                print(f"⏳ Model loading... Retry {attempt + 1}/{max_retries}")
                import time
                time.sleep(5)
                continue
                
            response.raise_for_status()
            result = response.json()
            
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "")
            return ""
            
        except Exception as e:
            print(f"❌ HF API Error (attempt {attempt + 1}): {e}")
            if attempt == max_retries - 1:
                raise
    
    return ""

def verify_content(text: str):
    """
    Verifies text using Hugging Face API + Serper search.
    """
    try:
        print(f"🤖 Processing with Hugging Face ({HF_MODEL})...")

        # 1. Get search context from Serper
        search_query = text[:200].replace("\n", " ")
        print(f"🔍 Searching Serper for: {search_query[:50]}...")
        search_context = search_web(search_query)
        
        if not search_context:
            search_context = "No external search results available."

        # 2. Construct prompt for fact-checking
        prompt = f"""You are a fact-checker. Analyze the following text against the search context and respond ONLY with valid JSON.

INPUT TEXT:
"{text}"

SEARCH CONTEXT:
{search_context}

Respond with this exact JSON format (no markdown, no code blocks):
{{
    "verified": true or false,
    "percentage": 0-100,
    "analysis": "detailed explanation",
    "errors": ["list any false claims"],
    "summary": "brief summary"
}}"""

        # 3. Call Hugging Face API
        response_text = call_huggingface_api(prompt)
        
        # 4. Clean and parse JSON
        response_text = response_text.replace("```json", "").replace("```", "").strip()
        
        # Try to extract JSON if wrapped in text
        if "{" in response_text and "}" in response_text:
            start = response_text.find("{")
            end = response_text.rfind("}") + 1
            response_text = response_text[start:end]
        
        result = json.loads(response_text)
        
        # Validate required fields
        if not all(key in result for key in ["verified", "percentage", "analysis", "errors", "summary"]):
            raise ValueError("Missing required fields in response")
            
        return result

    except json.JSONDecodeError as e:
        print(f"⚠️ JSON Parse Error: {e}")
        # Fallback response
        return {
            "verified": False,
            "percentage": 50,
            "analysis": f"AI response could not be parsed. Raw: {response_text[:200]}",
            "errors": ["JSON parsing failed"],
            "summary": "Verification incomplete"
        }
    except Exception as e:
        print(f"❌ Verification Error: {e}")
        return {
            "verified": False,
            "percentage": 0,
            "analysis": str(e),
            "errors": ["System error"],
            "summary": "Verification failed"
        }

def verify_content_with_image(image_bytes):
    """
    Image verification not supported in free cloud deployment.
    """
    return {
        "verified": False,
        "percentage": 0,
        "errors": ["Image verification requires local deployment with LLaVA model"],
        "analysis": "Image analysis is not available in cloud deployment. Please use text or PDF files.",
        "summary": "Image verification unavailable"
    }
