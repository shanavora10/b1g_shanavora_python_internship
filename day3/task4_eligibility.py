Age = int(input("Enter your age:"))
has_id = input("do you have a valid id? (yes/no):").lower()

if Age > 18 and has_id =="yes":
    print("Eligible")
else:
    print("Not Eligible")

