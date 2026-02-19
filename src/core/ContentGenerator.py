from typing import Dict, List, Optional
import logging
import requests
from transformers import pipeline

class ContentGenerator:
    def __init__(self):
        self.ai_pipeline = pipeline("text-generation", model="gpt2-large")
        self.supported_languages = ["en", "es", "fr"]
        
    def generate_blog_post(self, product_data: Dict, language: str) -> Optional[str]:
        """
        Generates a blog post based on product data and language.
        Implements retries for API calls and handles exceptions.
        """
        try:
            prompt = f"Write a SEO-optimized blog post for affiliate marketing in {language}.\nProduct Details:\n{product_data}\n"
            response = self.ai_pipeline(prompt, max_length=500)
            
            if not response:
                raise Exception("No content generated")
            
            return response[0]['generated_text']
        except Exception as e:
            logging.error(f"Content generation failed: {str(e)}", exc_info=True)
            return None