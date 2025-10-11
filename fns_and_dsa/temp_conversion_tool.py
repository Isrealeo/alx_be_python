FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def converts_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def converts_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temperature = float(input("Enter the temperature to convert"))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if sccale == "F":
    result  = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
elif scale == "C":
    result  = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.") 
    


