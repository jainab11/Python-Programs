# 2. Sum of three Integer adds to ZERO
# a. Desc -> A program with cubic running time. Read in N integers and counts the
# number of triples that sum to exactly 0.
# b. I/P -> N number of integer, and N integer input array
# c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
# d. O/P -> One Output is number of distinct triplets as well as the second output is to
# print the distinct triplets.
def triplets_zero(arr):
    found = False
    n = len(arr)
    # sort array
    arr.sort()
    for i in range(n-1):
        # initilize left and right
        left = i+1
        rigth = n-1
        num = arr[i]
        while (left<rigth) :
            if (num + arr[left]+arr[rigth]==0):
                print(f"{num},{arr[left]},{arr[rigth]}")
                left +=1
                rigth -=1
                found = True
            elif (num +arr[left]+arr[rigth] < 0):
                left +=1
            else:
                rigth -=1
            
    if (found == False):
        print("Triplets of number not found")

def main():
    N = int(input("Enter number of elements you want in array: "))
    elements = []
    for num in range(N):
        number = int(input(f"Enter an element {num + 1}: "))
        elements.append(number)

    print("Elements:", elements)
    triplets_zero(elements)  # Call the function to find triplets

if __name__ == "__main__":
    main()
