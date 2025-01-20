"""
Main script to run HumanEval evaluation.
"""
import os
import logging
import argparse
from datetime import datetime
from human_eval.data import read_problems, HUMAN_EVAL
from human_eval.evaluation import evaluate_functional_correctness
from evaluators.lmstudio import LMStudioEvaluator
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", default="results/codellama_test")
    parser.add_argument("--test_mode", action="store_true")
    parser.add_argument("--request_delay", type=float, default=5.0)
    parser.add_argument("--k", default="1", help="Comma-separated pass@k values")
    parser.add_argument("--timeout", type=float, default=3.0)
    args = parser.parse_args()
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(args.output_dir, timestamp)
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize evaluator
    evaluator = LMStudioEvaluator(
        output_dir=output_dir,
        request_delay=args.request_delay
    )
    
    # Load problems
    logger.info("Loading HumanEval problems...")
    problems = read_problems()
    
    # Create a temporary problem file for test mode
    problem_file = HUMAN_EVAL
    if args.test_mode:
        logger.info("Test mode: using first problem")
        first_key = sorted(problems.keys())[0]
        problems = {first_key: problems[first_key]}
        # Save reduced problem set
        problem_file = os.path.join(output_dir, "test_problems.jsonl")
        with open(problem_file, "w") as f:
            f.write(json.dumps(problems[first_key]) + "\n")
    
    # Get k values
    k_values = [int(k) for k in args.k.split(",")]
    max_k = max(k_values)
    
    # Generate samples
    samples_path = os.path.join(output_dir, "samples.jsonl")
    logger.info(f"Generating {max_k} samples per problem...")
    evaluator.run_evaluation(
        problems=problems,
        output_path=samples_path,
        num_samples_per_problem=max_k
    )
    
    # Run functional correctness evaluation
    logger.info("Evaluating functional correctness...")
    results = evaluate_functional_correctness(
        sample_file=samples_path,
        k=k_values,
        n_workers=1,  # Using 1 worker for stability
        timeout=args.timeout,
        problem_file=problem_file  # Use our problem set
    )
    
    # Log results
    logger.info("Evaluation Results:")
    for k, score in results.items():
        logger.info(f"{k}: {score:.3f}")
    
    logger.info(f"Evaluation complete. Results saved to {output_dir}")
    logger.info(f"- Samples: {samples_path}")
    logger.info(f"- Detailed results: {samples_path}_results.jsonl")

if __name__ == "__main__":
    main() 