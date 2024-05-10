# # Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
# Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
# can be found using a formula (Note: Take a, b and c as input values)
# delta = b*b - 4*a*c
# Root 1 of x = (-b + sqrt(delta))/(2*a)
# Root 2 of x = (-b - sqrt(delta))/(2*a)
import math
def find_roots(a,b,c):
    delta = b*b - 4*a*c
    if delta > 0:
        Root1 = (-b + math.sqrt(delta))/(2*a)
        Root2 = (-b - math.sqrt(delta))/(2*a)
        print(" Root 1 of x = ", Root1)
        print(" Root 2 of x = " , Root2)
    elif delta == 0:
        root = -b/(2*a)
        print("Root of x is " , root)
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(-delta)/(2*a)
        print(f"Root 1 of x = {real_part:.2f} + {imaginary_part:.2f} ")
        print(f"Root 2 of x = {real_part:.2f} - {imaginary_part:.2f} ")

def main():
    a = int(input("Enter a value of a : "))
    b = int(input("Enter a value of b : "))
    c = int(input("Enter a value of c : "))
    find_roots(a,b,c)
    
if __name__ == "__main__":
    main()