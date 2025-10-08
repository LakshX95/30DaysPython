# dct={"key1":"value1", "Key2":"value2", "key3":"value3"}
# print(dct)

# person ={"name":"Amal",
#          "age": "30",
#          "city": "Colombo",
#          "skills": ["Python", "Java", "Javascript"],
#          "is_Married":True
#          }

# print(person.get("name"))

# print(person.pop("age"))

dog = {
    "name": "Bella",
    "color": "Tan",
    "breed": "German Shephard",
    "legs": 4,
    "age": 5,
}

student = {
    "first_name": "Lakshan",
    "last_name": "Perera",
    "gender": "male",
    "age": 25,
    "marital_status": "single",
    "skills": ["Java", "C++", "Python"],
    "country": "Sri Lanka",
    "city": "Colombo",
    "address": "No. 123, Main Street",
}
print(len(student))
print(type(student.get("skills")))

student["skills"].append("Dart")
student["skills"].append("Flutter")
print(student["skills"])

print(student.keys())

print(student.values())

print(student.items())

del student["marital_status"]
del student["last_name"]
print(student)


print(dog)
del dog
print(dog)