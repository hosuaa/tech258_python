# Dictionaries

# key value pairs
# key is the reference, value is the actual data

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up", "collections"]
}

print(student1["stream"])
print(student1["completed_lesson_names"][1])
student1["completed_lessons"] = 3
print(student1)
student1["completed_lesson_names"].remove("collections")

print(student1.keys())
print(student1.values())
