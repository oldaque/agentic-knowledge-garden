---
name: "Response Accuracy Evaluation"
objective: "Calculates a basic accuracy score for AI agent responses based on exact string matching."
how_to_run: "This is a simple Python function. You can run it directly in a Python environment to see the example usage."
from_note: "../patterns/evaluation-and-monitoring.md"
---
def evaluate_response_accuracy(agent_output: str, expected_output: str) -> float:
    """Calculates a simple accuracy score for agent responses."""
    # This is a very basic exact match; real-world would use more sophisticated metrics
    return 1.0 if agent_output.strip().lower() == expected_output.strip().lower() else 0.0

# Example usage
agent_response = "The capital of France is Paris."
ground_truth = "Paris is the capital of France."
score = evaluate_response_accuracy(agent_response, ground_truth)
print(f"Response accuracy: {score}")
