# Garden Guardian - Data Engineering for Smart Agriculture

## Overview
**Garden Guardian** focuses on resilient data pipeline engineering and exception handling in Python 3.10+. This module covers catching built-in errors, raising custom exceptions, understanding inheritance in error handling, and ensuring resource cleanup using `try`/`except`/`finally` blocks within smart agricultural IoT scenarios.

---

## Technical Requirements & Guidelines

* **Language:** Python 3.10+
* **Code Style:** Must strictly follow the `flake8` linter standard.
* **Type Hinting:** Mandatory across all functions (`mypy` compliant).
* **Execution & Structure:**
  * All exercises require standard `try`/`except`/`finally` exception handling logic.
  * Programs must handle edge cases gracefully without crashing.
  * Appropriate use of built-in exceptions (`ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`) and custom exceptions.

---

## Exercises Summary

| Exercise | Directory | Submitted File(s) | Primary Concept | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Ex 00** | `ex0/` | `ft_first_exception.py` | Basic Exception Catching | Handles temperature string conversion and catches parsing failures using `try/except`. |
| **Ex 01** | `ex1/` | `ft_raise_exception.py` | Raising Exceptions (`raise`) | Validates temperature range bounds ($0^\circ\text{C}$ to $40^\circ\text{C}$) and raises range-specific errors. |
| **Ex 02** | `ex2/` | `ft_different_errors.py` | Multi-Exception Handling | Demonstrates catching `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, and `TypeError`. |
| **Ex 03** | `ex3/` | `ft_custom_errors.py` | Custom Exception Hierarchy | Defines custom `GardenError`, `PlantError`, and `WaterError` classes with inheritance. |
| **Ex 04** | `ex4/` | `ft_finally_block.py` | Guaranteed Cleanup (`finally`) | Implements watering validation and uses `finally` to ensure system resource closure. |

---

## Exercise Details

### Exercise 00: Agricultural Data Validation
* **Concepts:** Basic error handling, string parsing, `ValueError`/`Exception` handling.
* **Details:** 
  * Implements `input_temperature(temp_str)` to parse temperature inputs to integers.
  * Implements `test_temperature()` to demonstrate successful parsing and catch invalid string conversion errors while keeping execution active.

### Exercise 01: Agricultural Data Validation Pipeline
* **Concepts:** Explicit exception raising (`raise Exception(...)`), range validation.
* **Details:** 
  * Enhances `input_temperature()` to validate values against a $0^\circ\text{C} - 40^\circ\text{C}$ threshold.
  * Raises detailed exceptions when input falls below $0^\circ\text{C}$ or exceeds $40^\circ\text{C}$.
  * Catches out-of-bounds error messages within `test_temperature()`.

### Exercise 02: Different Types of Problems
* **Concepts:** Categorized exception catching, explicit exception handling patterns.
* **Details:** 
  * Implements `garden_operations(operation_number)` triggering distinct error conditions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError`).
  * Implements `test_error_types()` to catch each error type individually or in groups and display dedicated failure summaries.

### Exercise 03: Making Your Own Error Types
* **Concepts:** Exception class inheritance, custom error messaging.
* **Details:** 
  * Constructs a custom base class `GardenError(Exception)` and specialized subclasses `PlantError(GardenError)` and `WaterError(GardenError)`.
  * Demonstrates that catching the base class `GardenError` successfully intercepts both `PlantError` and `WaterError` instances.

### Exercise 04: Finally Block - Always Clean Up
* **Concepts:** Resource cleanup, execution flow control via `finally`.
* **Details:** 
  * Implements `water_plant(plant_name)` which validates capitalization (raising `PlantError` if uncapitalized).
  * Implements `test_watering_system()` which opens watering pipelines, executes plant checks, handles failures, and guarantees system shutdown inside a `finally:` block.

---

## Testing & Quality

### Linter & Type Checks
Ensure strict adherence to `flake8` guidelines and static typing via `mypy`:
```bash
flake8 .
mypy ex4/ft_finally_block.py
