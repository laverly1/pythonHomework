def convert_cel_to_far(celsius: float) -> float:
    """Converts Celsius to Fahrenheit."""
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius."""
    return round((fahrenheit - 32) * 5/9, 2)

def main():
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {celsius} degrees C\n")
    
    celsius = float(input("Enter a temperature in degrees C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {fahrenheit} degrees F")

if __name__ == "__main__":
    main()
