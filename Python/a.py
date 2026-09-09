def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    while True:
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} °C is {fahrenheit:.2f} °F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} °F is {celsius:.2f} °C")
        elif choice == '3':
            print("Exiting the converter. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Entry point correction
if __name__ == "__main__":
    main()
