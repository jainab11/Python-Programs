def harmonic_number(num):
    if num == 0:
        print("number should not be zero")
        
        return
    sum = 0.0
    for i in range(1,num+1):
        sum += 1/i
    return sum
number = int(input("enter a number : "))
print(harmonic_number(number))