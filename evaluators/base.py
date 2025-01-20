"""
Base evaluator class for code generation models.
"""
import json
import os
from typing import Dict, List, Any
from abc import ABC, abstractmethod
import logging
from human_eval.data import write_jsonl

logger = logging.getLogger(__name__)

class BaseEvaluator(ABC):
    def __init__(self, output_dir: str = "results/base"):
        """Initialize base evaluator."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    @abstractmethod
    def generate_completion(self, prompt: str) -> str:
        """Generate code completion for a given prompt."""
        raise NotImplementedError
        
    def run_evaluation(
        self,
        problems: Dict[str, Any],
        output_path: str,
        num_samples_per_problem: int = 1
    ) -> List[Dict[str, Any]]:
        """Run evaluation with k samples per problem."""
        logger.info(f"Evaluating {len(problems)} problems with {num_samples_per_problem} samples each...")
        
        samples = []
        for task_id, problem in problems.items():
            logger.info(f"Processing task {task_id}")
            
            # Generate k samples for this problem
            for sample_idx in range(num_samples_per_problem):
                completion = self.generate_completion(problem["prompt"])
                sample = {
                    "task_id": task_id,
                    "completion": completion,
                    "completion_id": sample_idx
                }
                samples.append(sample)
                logger.info(f"Completed task {task_id} sample {sample_idx + 1}/{num_samples_per_problem}")
        
        # Write all samples
        write_jsonl(output_path, samples)
        return samples 