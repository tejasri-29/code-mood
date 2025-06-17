def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Conversion Program")
    print("Available units: Celsius (C), Fahrenheit (F), Kelvin (K)")

    while True:
        try:
            temp_str = input("Enter the temperature value: ")
            temperature = float(temp_str)
            unit = input("Enter the original unit (C, F, or K): ").upper()

            if unit == 'C':
                fahrenheit = celsius_to_fahrenheit(temperature)
                kelvin = celsius_to_kelvin(temperature)
                print(f"{temperature}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K")
            elif unit == 'F':
                celsius = fahrenheit_to_celsius(temperature)
                kelvin = fahrenheit_to_kelvin(temperature)
                print(f"{temperature}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K")
            elif unit == 'K':
                celsius = kelvin_to_celsius(temperature)
                fahrenheit = kelvin_to_fahrenheit(temperature)
                print(f"{temperature}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F")
            else:
                print("Invalid unit entered. Please enter C, F, or K.")
                continue

            another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
            if another_conversion != 'yes':
                break

        except ValueError:
            print("Invalid temperature value. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
