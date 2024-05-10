# Write a program WindChill.java that takes two double command-line arguments t
# and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
# temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
# National Weather Service defines the effective temperature (the wind chill) to be:
# Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
# than 120 or less than 3 (you may assume that the values you get are in that range)
import math
def wind_chill(temp, speed):
    if abs(temp) > 50 or speed > 120 or speed < 3:
        print("Invalid input values. Temperature must be less than 50 in absolute value, and wind speed must be between 3 and 120.")
        return None

    wind_chill = 35.74 + 0.6215 * temp - 35.75 * math.pow(speed, 0.16) + 0.4275 * temp * math.pow(speed, 0.16)
    return wind_chill

def main():
    temp = float(input("Enter the temperature (in Fahrenheit): "))
    speed = float(input("Enter the wind speed (in miles per hour): "))

    result = wind_chill(temp, speed)
    if result is not None:
        print("Wind chill:", result)

if __name__ == "__main__":
    main()
