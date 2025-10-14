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
