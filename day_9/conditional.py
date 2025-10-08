# # # age = input("Enter your age: ")

# # # if int(age) >= 18: 
# # #     print("you area old enough to drive") 
# # # else :
# # #     years_ledt = 18 - int(age)
# # #     print("wait for the " + str(years_ledt) + " years")


# # # num1 = int(input("Enter number 1: "))
# # # num2 = int(input("Enter number 2: "))

# # # if num1 > num2:
# # #     print(str(num1) + " is greater than " + str(num2))
# # # elif num1 < num2:
# # #     print(str(num1) + " is less than " + str(num2))
# # # else:
# # #     print(str(num1) + " is equal to " + str(num2))


# # score = int(input("Enter your score: "))    

# # if score >= 80 and score <= 100:
# #     print("A")
# # elif score >= 70 and score < 89:
# #     print("B")
# # elif score >= 60 and score < 69:
# #     print("C")  
# # elif score >= 50 and score < 59:
# #     print("D")
# # elif score >= 0 and score < 49:
# #     print("F")

# month = input("Enter the month: ").lower()

# if month in["september", "october", "november"] :
#     print("This is Autumn Season!")
# elif month in ["december", "january", "february"] :
#     print("This is Winter!")
# elif month in ["march", "april", "may"]:
#     print("this is Spring!")
# else:
#     print("This is Summer!!!")


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

print(person['skills'])

skills = person['skills']
mid_index = len(skills) // 2
print("middle skill:", skills[mid_index])

if "python" in skills:
    print("yes, python is in hiss skill list")
else:
    print("No, python is not in the skill")
