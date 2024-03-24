while True:
    temperature = input("Enter the temperature in Fahrenheit: ")
    try:
        celsius = (int(temperature) - 32) * 5/9
        print(f"The temperature in Celsius is {celsius:.2f}")
        break
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("Please enter a number other than zero.")
    except Exception as e:
        print("An error occurred.")
        print(e)
    finally:
        print("Thank you for using the temperature converter.")