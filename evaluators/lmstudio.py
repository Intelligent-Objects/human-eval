"""
LM Studio evaluator for code generation.
"""
import logging
import time
from typing import Dict, Optional, List, Any
from evaluators.base import BaseEvaluator
from utils import make_api_request, format_prompt, extract_code
from config import SERVER_CONFIG, MODEL_CONFIG

logger = logging.getLogger(__name__)

class LMStudioEvaluator(BaseEvaluator):
    def __init__(
        self,
        output_dir: str = "results/codellama_test",
        server_config: Optional[Dict] = None,
        model_config: Optional[Dict] = None,
        request_delay: float = 0.5  # Reduced to 0.5s minimum delay
    ):
        """Initialize LM Studio evaluator."""
        super().__init__(output_dir)
        self.server_config = server_config or SERVER_CONFIG
        self.model_config = model_config or MODEL_CONFIG
        self.request_delay = request_delay
        self.last_request_time = 0
        
    def generate_completion(self, prompt: str) -> str:
        """Generate code completion."""
        time.sleep(self.request_delay)  # Simple fixed delay between requests
        
        try:
            response = make_api_request(
                url=self.server_config["base_url"],
                endpoint=self.server_config["endpoint"],
                payload={
                    "model": self.model_config["model"],
                    "prompt": format_prompt(prompt),
                    **self.model_config["generation_params"]
                },
                headers=self.server_config["headers"],
                timeout=self.server_config["timeout"]
            )
            return response["choices"][0]["text"]
            
        except Exception as e:
            logger.error(f"Failed to generate completion: {str(e)}")
            return ""
            
    def run_evaluation(
        self,
        problems: Dict[str, Any],
        output_path: str,
        num_samples_per_problem: int = 1
    ) -> List[Dict[str, Any]]:
        """Run evaluation."""
        logger.info("Starting evaluation...")
        return super().run_evaluation(
            problems=problems,
            output_path=output_path,
            num_samples_per_problem=num_samples_per_problem
        ) 