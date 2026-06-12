#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hello" + 5
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    try:
        print("Testing operation 0...")
        garden_operations(0)
        print("Operation completed successfully")
    except ValueError as error:
        print(f"Caught ValueError error: {error}")

    try:
        print("Testing operation 1...")
        garden_operations(1)
        print("Operation completed successfully")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError error: {error}")

    try:
        print("Testing operation 2...")
        garden_operations(2)
        print("Operation completed successfully")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError error: {error}")

    try:
        print("Testing operation 3...")
        garden_operations(3)
        print("Operation completed successfully")
    except TypeError as error:
        print(f"Caught TypeError error: {error}")

    try:
        print("Testing operation 4...")
        garden_operations(4)
        print("Operation completed successfully")
    except Exception as error:
        print(f"Unexpected error: {error}")

    try:
        print("Testing multiple exception catch...")
        garden_operations(0)
    except (ValueError, TypeError) as error:
        print(f"Caught multiple error types: {error}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
