---
name: "Learning and Adaptation with OpenEvolve"
objective: "Demonstrates how to use the OpenEvolve library to optimize a program through evolutionary algorithms."
how_to_run: "Requires the OpenEvolve library and initial program, evaluator, and config files. Run with `python your_script_name.py`."
from_note: "../patterns/learning-and-adaptation.md"
---

# Learning and Adaptation with OpenEvolve

This snippet shows how to use the `OpenEvolve` library to automatically improve a program based on a given evaluation function. This is a powerful technique for learning and adaptation in AI systems.

## Code Example

```python
from openevolve import OpenEvolve

# Initialize the system
evolve = OpenEvolve(
    initial_program_path="path/to/initial_program.py",
    evaluation_file="path/to/evaluator.py",
    config_path="path/to/config.yaml"
)

# Run the evolution
best_program = await evolve.run(iterations=1000)
print(f"Best program metrics:")
for name, value in best_program.metrics.items():
    print(f" {name}: {value:.4f}")
```

## How It Works

- The `OpenEvolve` class is initialized with paths to the initial program, an evaluation script, and a configuration file.
- The `run` method executes the evolutionary optimization process for a specified number of iterations.
- The system iteratively modifies and evaluates the program, seeking to improve its performance based on the metrics defined in the evaluator.
- Finally, the metrics of the best-performing program are printed.