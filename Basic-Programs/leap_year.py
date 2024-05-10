def check_leap_year(number):
    if number.isdigit():
        number = int(number)
        if (number % 4 == 0 and number % 100 != 0)or number % 400 == 0:
            print(f"yes, This year {number} is leap year.")
        else:
            print(f"No, This year {number} is not a leap year.")
    else:
        print("input should be valid")
year = input("Enter a year : ")
check_leap_year(year)
