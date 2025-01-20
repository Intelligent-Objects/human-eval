"""
Utility functions for the evaluation framework.
"""
import logging
import requests
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class APIError(Exception):
    """Custom exception for API errors."""
    pass

def make_api_request(
    url: str,
    endpoint: str,
    payload: Dict[str, Any],
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 240
) -> Dict[str, Any]:
    """Make API request with logging."""
    try:
        full_url = f"{url}{endpoint}"
        logger.info(f"Making request to: {full_url}")
        logger.debug(f"Payload: {payload}")
        
        response = requests.post(
            full_url,
            json=payload,
            headers=headers,
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"API request failed: {str(e)}")
        raise APIError(f"API request failed: {str(e)}")

def format_prompt(prompt: str) -> str:
    """Pass prompt directly to the server."""
    return prompt

def extract_code(completion: str) -> str:
    """Pass completion directly from server to @human_eval."""
    return completion 