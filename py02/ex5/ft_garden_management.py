class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        if plant_name == "" or plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print("Added " + plant_name + " successfully")

    def water_plants(self):
        try:
            print("Opening watering system")
            for plant in self.plants:
                print("Watering " + plant + "- success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        if water_level > 10:
            raise ValueError("Water level " + str(water_level) + " is too high (max 10)")
        if water_level < 1:
            raise ValueError("Water level " + str(water_level) + " is too low (min 1)")
        if sunlight_hours > 12:
            raise ValueError("Sunlight hours " + str(sunlight_hours) + " is too high (max 12)")
        if sunlight_hours < 2:
            raise ValueError("Sunlight hours " + str(sunlight_hours) + " is too low (min 2)")
        print(plant_name + ": healthy (water: " + str(water_level) + ", sun: " + str(sunlight_hours) + ")")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()

    print()
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
    except ValueError as e:
        print("Error adding plant:", e)
    try:
        garden.add_plant("lettuce")
    except ValueError as e:
        print("Error adding plant:", e)
    try:
        garden.add_plant("")
    except ValueError as e:
        print("Error adding plant:", e)

    print()
    print("Watering plants...")
    garden.water_plants()

    print()
    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print("Error checking tomato:", e)
    try:
        garden.check_plant_health("lettuce", 15, 6)
    except ValueError as e:
        print("Error checking lettuce:", e)

    print()
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError:", e)
    print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()