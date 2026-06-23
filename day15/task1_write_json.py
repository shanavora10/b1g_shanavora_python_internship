import json 

student_dict = {
    "name": "john",
    "marks": 85
}

with open("student.json","w") as file:
    json.dump(student_dict, file, indent=4)

print("Data successfully saved to student.json!")

