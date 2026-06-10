#sample list
numbers =[45,10,89,3,56,90,12]
print(f"List: {numbers}\n")

# Method1
built_in_max =max(numbers)
built_in_min =min(numbers)
print("---Method 1 (Using-in Functions) ---")
print("Max=",built_in_max)
print("Min=",built_in_min)

# Method2
largest =numbers[0]
smallest =numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("---Method 2 (Manual loop) ---")
print("Max=",largest)
print("Min=",smallest)