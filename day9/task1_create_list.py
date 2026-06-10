numbers =[]

print("Please enter 5 numbers:")

for i in range(1,6):
    num =int(input(f"your list of number {i}:"))
    numbers.append(num)

print("-" * 30)
print("Your list of numbers:",numbers)

