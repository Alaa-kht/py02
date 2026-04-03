#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print()
    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        test_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        test_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()