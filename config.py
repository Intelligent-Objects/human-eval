"""
Configuration settings for the evaluation framework.
"""

# Server configuration
SERVER_CONFIG = {
    "base_url": "http://10.5.0.2:1234",
    "timeout": 240,
    "headers": {"Content-Type": "application/json"},
    "endpoint": "/v1/completions"
}

# Model configuration matching LM Studio settings
MODEL_CONFIG = {
    "model": "codellama-13b-python",
    "generation_params": {
        "temperature": 0.1,
        "top_k": 50,
        "top_p": 0.95,
        "repeat_penalty": 1.1,
        "max_tokens": 512,  # Reduced for more focused completions
        "stream": False
    }
}

# Evaluation settings
EVAL_CONFIG = {
    "num_workers": 1,
    "timeout": 3.0,  # Match @human_eval default
    "k_values": [1]
} 