# # 3. Write a program Distance.java that takes two integer command-line arguments x
# and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
# formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
import math
def distance(num1, num2):
    return math.sqrt(num1 ** 2 + num2 ** 2)

def main():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    print(f"Eculidean distance of {x}, {y}  to the origin(0,0) is {distance(x, y)}  ")

if __name__ == "__main__":
    main()