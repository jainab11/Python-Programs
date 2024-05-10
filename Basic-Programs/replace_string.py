user_name = input("Enter your name : ")

while len(user_name)<3:
    print("name should have at least 3 character")
    break

print(f"Hello {user_name}, How are you")

