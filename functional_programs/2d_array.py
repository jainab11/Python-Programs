# writing function for reading array
def read_2d_array(rows,cols):
    array =[]
    for rowss in range(rows):
        row =[]
        for colss in range(cols):
            element = int(input(f" Enter element at position ({rowss+1},{colss+1})"))
            row.append(element)
        array.append(row)
    return array
        
# function for printing 2d array
def print_2d_array(array):
    for row in array:
        print(" ".join(map(str,row)))
# take input frrom user
def main():
    row = int(input("Enter number of rows : "))
    col = int(input("Enter number of cols : "))
    arrays = read_2d_array(row,col)
    print("2D array is:")
    print_2d_array(arrays)
if __name__ == "__main__":
    main()
    