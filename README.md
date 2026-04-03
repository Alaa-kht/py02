# py02 - Garden Guardian: Data Engineering for Smart Agriculture

## Project Overview

Garden Guardian is a Python project focused on learning and demonstrating
error handling techniques through a garden-themed programming context.
The project covers built-in exceptions, raising exceptions, custom
exceptions, and the `finally` block.

## Project Structure
py02/
├── ex0/
│   └── ft_first_exception.py
├── ex1/
│   └── ft_raise_exception.py
├── ex2/
│   └── ft_different_errors.py
├── ex3/
│   └── ft_custom_errors.py
├── ex4/
│   └── ft_finally_block.py
└── README.md

## Exercises

### Exercise 0 - Agricultural Data Validation (`ft_first_exception.py`)

Introduces basic exception handling with `try/except`:

- `input_temperature(temp_str)` converts a string to an integer temperature
- `test_temperature()` tests valid and invalid inputs
- Demonstrates that the program keeps running after catching an error

### Exercise 1 - Validation Pipeline (`ft_raise_exception.py`)

Extends Exercise 0 with the `raise` keyword:

- Validates temperature is within plant-safe range (0 to 40°C)
- Raises `ValueError` with a descriptive message for out-of-range values
- Tests extreme values like `"100"` and `"-50"`

### Exercise 2 - Different Error Types (`ft_different_errors.py`)

Demonstrates handling of Python's built-in exception types:

- **ValueError** - Invalid data conversion (e.g., `int("abc")`)
- **ZeroDivisionError** - Division by zero
- **FileNotFoundError** - Opening a non-existent file
- **TypeError** - Mixing incompatible types
- Catching multiple error types with a single `try` block

### Exercise 3 - Custom Errors (`ft_custom_errors.py`)

Creates custom exception classes using inheritance:

- **GardenError** - Base exception for all garden problems
- **PlantError** - Specific exception for plant issues
- **WaterError** - Specific exception for watering issues
- Demonstrates that catching a parent exception catches all child exceptions

### Exercise 4 - Finally Block (`ft_finally_block.py`)

Shows how `finally` ensures cleanup always runs:

- `water_plant(plant_name)` succeeds only if the name is capitalized
- `test_watering_system()` opens/closes the watering system using `finally`
- Cleanup always happens whether or not an error occurred

## How to Run
```bash
python ex0/ft_first_exception.py
python ex1/ft_raise_exception.py
python ex2/ft_different_errors.py
python ex3/ft_custom_errors.py
python ex4/ft_finally_block.py
```

## Key Concepts Learned

- **try/except** - Catching and handling exceptions gracefully
- **raise** - Throwing exceptions when invalid data is detected
- **try/except/finally** - Ensuring cleanup code always executes
- **Custom Exceptions** - Domain-specific error types via class inheritance
- **Exception Hierarchy** - Using parent exceptions to catch related errors

## Requirements

- Python 3.10+
- flake8 (linting)
- mypy (type checking)