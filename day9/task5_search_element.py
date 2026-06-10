numbers =[12,45,78,23,56,89]
print("Available numbers:",numbers)

target =int(input("Enter  number to search:"))

#Method1
print("\n---Method 1 (in operation) ---")
if target in numbers:
    position =numbers.index(target)
    print("Found at index",position)
else:
    print("Not Found")

#Method2
print("\n---Method 2 (Manual Loop) ---")
found = False
found_index =-1

for i in range(len(numbers)):
    if numbers[i] ==target:
        found =True
        found_index =i
        break
if found:
    print("Found at index",found_index)
else:
    print("Not Found")
    