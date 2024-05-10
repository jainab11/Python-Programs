def power_of_2(number):
    if number >=31 and number <=0:
        print("out of integer range. ")
        return
    for i in range( 1 , number+1):
        result = 2**i
        print(f"2^{i} = {result} ")
num = int(input("Enter a number : "))
power_of_2(num)
        