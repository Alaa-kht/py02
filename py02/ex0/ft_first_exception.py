def check_temperature(temp_str):
    try:
        temp_int = int(temp_str)
    except ValueError:
        print("Error: '" + temp_str + "' is not a valid number")
        return None

    if temp_int < 0:
        print("Error: '" + temp_str + "°C' is too cold for plants (min 0°C)")
        return None

    if temp_int > 40:
        print("Error: '" + temp_str + "°C' is too hot for plants (max 40°C)")
        return None

    print("Temperature is " + str(temp_int) + "°C is perfect for plants!")
    return temp_int


def test_temperature():
    print("=== Garden Temperature Checker ===")

    print("Testing temperature: 25")
    check_temperature("25")

    print("Testing temperature: abc")
    check_temperature("abc")

    print("Testing temperature: 100")
    check_temperature("100")

    print("Testing temperature: -50")
    check_temperature("-50")

    print("All tests completed — program didn't crash!")


if __name__ == "__main__":
    test_temperature()
