class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def check_plant(plant, status):
    if status == "wilting":
        raise PlantError("The tomato plant is wilting!")

def check_water(level):
    if level < 10:
        raise WaterError("Not enough water in the tank!")

def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print()
    print("Testing PlantError...")
    try:
        check_plant("tomato", "wilting")
    except PlantError as e:
        print("Caught PlantError:", e)

    print()
    print("testing WaterError...")
    try:
        check_water(5)
    except WaterError as e:
        print("Caught WaterError:", e)

    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", "wilting")
    except GardenError as e:
        print("caught a garden error:", e)
    try:
        check_water(5)
    except WaterError as e:
        print("Caught a garden error:", e)

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
