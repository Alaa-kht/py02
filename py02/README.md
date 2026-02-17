# Garden Guardian - Error Handling in Python

## Project Overview

Garden Guardian is a Python project focused on learning and demonstrating error handling techniques through a garden-themed programming context. The project covers built-in exceptions, custom exceptions, the `finally` block, the `raise` keyword, and a full integration exercise combining all concepts.

## Project Structure

```
py02/
├── ex1/
│   └── ft_different_errors.py
├── ex2/
│   └── ft_custom_errors.py
├── ex3/
│   └── ft_finally_block.py
├── ex4/
│   └── ft_raise_errors.py
├── ex5/
│   └── ft_garden_management.py
└── README.md
```

## Exercises

### Exercise 1 - Different Error Types (`ft_different_errors.py`)

Demonstrates how to handle Python's built-in exception types:

- **ValueError** - Handling invalid data conversion (e.g., converting `"abc"` to an integer)
- **ZeroDivisionError** - Handling division by zero
- **FileNotFoundError** - Handling attempts to open non-existent files
- **KeyError** - Handling missing dictionary keys
- Catching multiple error types with a single `except` block

### Exercise 2 - Custom Errors (`ft_custom_errors.py`)

Introduces custom exception classes using inheritance:

- **GardenError** - Base exception class for all garden-related problems
- **PlantError** - Specific exception for plant issues (inherits from `GardenError`)
- **WaterError** - Specific exception for watering issues (inherits from `GardenError`)
- Demonstrates that catching a parent exception also catches its child exceptions

### Exercise 3 - The Finally Block (`ft_finally_block.py`)

Shows how `finally` ensures cleanup code always runs:

- Simulates opening and closing a watering system
- Demonstrates cleanup execution on successful operations
- Demonstrates cleanup execution even when errors occur
- Uses the `try/except/finally` structure

### Exercise 4 - Raising Errors (`ft_raise_errors.py`)

Demonstrates how to raise exceptions with the `raise` keyword:

- Validates plant names (must not be empty)
- Validates water levels (must be between 1 and 10)
- Validates sunlight hours (must be between 2 and 12)
- Provides helpful, descriptive error messages

### Exercise 5 - Garden Management System (`ft_garden_management.py`)

A comprehensive integration exercise combining all techniques:

- Implements a `GardenManager` class with methods for adding plants, watering, and health checks
- Uses custom exceptions (`GardenError`, `PlantError`, `WaterError`)
- Applies `try/except/finally` blocks for resource management
- Raises errors for invalid input with descriptive messages
- Demonstrates error recovery and system resilience

## How to Run

```bash
python3 ex1/ft_different_errors.py
python3 ex2/ft_custom_errors.py
python3 ex3/ft_finally_block.py
python3 ex4/ft_raise_errors.py
python3 ex5/ft_garden_management.py
```

## Key Concepts Learned

- **try/except** - Catching and handling exceptions gracefully
- **try/except/finally** - Ensuring cleanup code always executes
- **raise** - Creating and throwing exceptions when problems are detected
- **Custom Exceptions** - Defining domain-specific error types using class inheritance
- **Exception Hierarchy** - Using parent exceptions to catch groups of related errors
- **Error Recovery** - Keeping programs running after handling errors

## Requirements

- Python 3.x
- No external libraries required

## Author

Data Engineering for Smart Agriculture - Garden Guardian Project