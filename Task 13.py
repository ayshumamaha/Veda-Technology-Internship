def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def main():
    print("Temperature Converter")
    print("Convert between Celsius, Fahrenheit, and Kelvin.")

    while True:
        print("\nChoose a conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        conversions = {
            "1": ("Celsius", "Fahrenheit", celsius_to_fahrenheit, False),
            "2": ("Celsius", "Kelvin", celsius_to_kelvin, False),
            "3": ("Fahrenheit", "Celsius", fahrenheit_to_celsius, False),
            "4": ("Fahrenheit", "Kelvin", fahrenheit_to_kelvin, False),
            "5": ("Kelvin", "Celsius", kelvin_to_celsius, True),
            "6": ("Kelvin", "Fahrenheit", kelvin_to_fahrenheit, True),
        }

        if choice not in conversions:
            print("Invalid choice. Please enter a number from 0 to 6.")
            continue

        from_unit, to_unit, converter, is_kelvin_input = conversions[choice]

        try:
            temperature = float(input(f"Enter temperature in {from_unit}: "))
        except ValueError:
            print("Invalid temperature. Please enter a number.")
            continue

        if is_kelvin_input and temperature < 0:
            print("Invalid temperature: Kelvin cannot be below absolute zero (0 K).")
            continue

        if from_unit == "Celsius" and temperature < -273.15:
            print("Invalid temperature: Celsius cannot be below -273.15 C.")
            continue

        if from_unit == "Fahrenheit" and temperature < -459.67:
            print("Invalid temperature: Fahrenheit cannot be below -459.67 F.")
            continue

        result = converter(temperature)
        print(f"{temperature:.2f} {from_unit} = {result:.2f} {to_unit}")


if __name__ == "__main__":
    main()
