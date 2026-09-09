def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32

while True:
    print("\nChoose conversion type:")
    print("1: Fahrenheit to Celsius")
    print("2: Celsius to Fahrenheit")
    print("Type 'exit' to quit")

    user_choice = input("Enter your choice (1/2) or 'exit': ").lower()

    if user_choice == 'exit':
        print("Exiting the program. Goodbye!")
        break

    elif user_choice == '1':
        fahrenheit = input("Enter temperature in Fahrenheit: ")
        if fahrenheit.replace('.', '', 1).isdigit() or (fahrenheit.startswith('-') and fahrenheit[1:].replace('.', '', 1).isdigit()):
            fahrenheit = float(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
        else:
            print("Invalid input. Please enter a valid number.")

    elif user_choice == '2':
        celsius = input("Enter temperature in Celsius: ")
        if celsius.replace('.', '', 1).isdigit() or (celsius.startswith('-') and celsius[1:].replace('.', '', 1).isdigit()):
            celsius = float(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
        else:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please enter 1, 2, or 'exit'.")
