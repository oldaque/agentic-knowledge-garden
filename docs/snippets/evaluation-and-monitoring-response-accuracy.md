---
name: "Response Accuracy Evaluation"
objective: "Calculates a basic accuracy score for AI agent responses based on exact string matching."
how_to_run: "This is a simple Python function. You can run it directly in a Python environment to see the example usage."
from_note: "../patterns/evaluation-and-monitoring.md"
---

## Explanation

This code provides a simple baseline implementation for evaluating AI agent response accuracy through exact string matching. The function normalizes both the agent output and expected output by stripping whitespace and converting to lowercase before comparison.

While this approach works for exact matches, it has limitations: it returns a binary score (1.0 for perfect match, 0.0 otherwise) and doesn't account for semantic equivalence, paraphrasing, or partial correctness. The example demonstrates this limitation - even though both responses convey the same information ("Paris is the capital of France"), they receive a score of 0.0 due to different word ordering.

In production systems, more sophisticated metrics should be used, such as BLEU scores for translation tasks, F1 scores for information extraction, semantic similarity using embeddings, or LLM-as-a-Judge for nuanced evaluations. This simple function serves as a foundation for understanding accuracy evaluation concepts.

## Code

```python
def evaluate_response_accuracy(agent_output: str, expected_output: str) -> float:
    """Calculates a simple accuracy score for agent responses."""
    # This is a very basic exact match; real-world would use more sophisticated metrics
    return 1.0 if agent_output.strip().lower() == expected_output.strip().lower() else 0.0

# Example usage
agent_response = "The capital of France is Paris."
ground_truth = "Paris is the capital of France."
score = evaluate_response_accuracy(agent_response, ground_truth)
print(f"Response accuracy: {score}")
```
