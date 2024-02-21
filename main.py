# Welcome Title.
print("Welcome to Zambia Travels Temperature Converter")

# Tagline.
print("Let us help you know the right temperature so you never have to be underdressed or uncomfortable.\n")

# Formula to convert from Celsius to Fahrenheit
def celsius_to_fahrenheit_formula (celsius):
    return (9 / 5) * celsius + 32

# Formula to convert from Fahrenheit to Celsius
def fahrenheit_to_celsius_formula (fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# While Loop to keep the app running.
while True:
    # Try-Except statement to ensure if user enters the wrong character like a letter the app will not crash.
    try:
        # Gets the users input for selecting an option.
        option_selector = int(input("Press 1 for Celsius to Fahrenheit \nPress 2 for Fahrenheit to Celsius\nPress 0 to exit\n"))

        if option_selector == 1:
            print("CELSIUS TO FAHRENHEIT")
            # While loop and try-except to ensure there are no errors when trying to convert.
            while True:
                try:
                    celsius_input = int(input("Enter in the Degrees Celsius:\n "))
                    conversion_answer = celsius_to_fahrenheit_formula(celsius_input)
                    print("Your answer is " + str(conversion_answer) + " Degrees Fahrenheit.\n")

                    break
                except ValueError:
                    print("Please enter a numerical character.\n")

        elif option_selector == 2:
            print("FAHRENHEIT TO CELSIUS")
            # While loop and try-except to ensure there are no errors when trying to convert.
            while True:
                try:
                    fahrenheit_input = int(input("Enter in the Degrees Fahrenheit:\n "))
                    conversion_answer = fahrenheit_to_celsius_formula(fahrenheit_input)
                    print("Your answer is " + str(conversion_answer) + " Degrees Celsius.\n")

                    break
                except ValueError:
                    print("Please enter a numerical character. Try again.\n")

        # This is the exit option
        elif option_selector == 0:
            print("Thank You for using our application. Good Day.\nExiting...")

            break

        # If user enters thee wrong nummerical option it will loop back.
        else:
            print("You've entered a wrong key. Please try again.\n")

    # If user enters a symbol or letter character, this prevents app from crashing.
    except ValueError:
        print("You've entered a wrong character, please use the number keys.\n")
