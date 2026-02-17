def garden_operations(operation):
    if operation == "Value":
        result = int("abc")
    elif operation == "Zero":
        result = 10 / 0
    elif operation == "file":
        f = open("missing.txt")
        f.close()
    elif operation == "Key":
        garden = {"rose": "red"}
        flower = garden["missing_plant"]

def test_error_types():
    print("=== Garden Error Types Demo ===")
    
    print()
    print("Testing ValueError...")
    try:
        garden_operations("Value")
    except ValueError as e:
        print("Caught ValueError:", e)

    print()
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("Zero")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    print()
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

    print()
    print("Testing KeyError...")
    try:
        garden_operations("Key")
    except KeyError as e:
        print("Caught KeyError:", e)

    print()
    print("Testing multiple errors together...")
    try:
        garden_operations("Value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
   
    print()
    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()

