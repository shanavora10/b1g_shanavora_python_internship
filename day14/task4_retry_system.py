while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. please enter numbers only.")

print(f"Thank you. your age is {age}." )
