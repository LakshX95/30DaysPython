# number = 1

# while number < 10:
#     print(number)
#     number = number + 1
#     if number == 6:
#         break

# count = 0

# while count < 8:
#     if count == 3:
#         count = count + 1 
#         continue
#     print(count)
#     count = count + 1

# language = "python"

# for letters in language:
#     print(letters)

# for i in range(len(language)):
#     print(language[i])

# numbers = (1, 2, 3, 4, 5, 6)

# for i in numbers:
#     print(i)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key,":", value)

numbers = (0, 1, 2, 3, 4, 5, 6)

# for i in numbers:
#     print(i)
#     if i == 3:
#         continue
#     print("next number should be", i+1)
# if i != 5:
#     print("loop's ended!")

# lst = list(range(11))
# print(lst)

# st = set(range(1,11))
# print(st)


# lst = set(range(0, 11, 3))
# print(lst)


# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# for key in person:
#     if key == "skills":
#         for skills in person['skills']:
#             print(skills)

# for i in range(11):
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# for i in range(10, 0, -1):
#     print(i)

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# symbol = "#"
# i = 1

# while i <= 10:
#     print(symbol)
#     i += 1

# for i in range(1, 8):
#     print(i*"#")

# for i in range(8):
#     for j in range(8):
#         print("#", end=" ")
#     print()

# for i in range(11):
#     print(i,"x",i, "=",i*i )

# for i in range(0, 100, 2):
#     print(i)

# for i in range(101):
#     if i % 2 != 0:
#         print(i)

# total = 0

# for i in range(101):

#     total += i
# print(total)

# sum_even = 0
# sum_odd = 0

# for i in range(101):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
# print("total sum of odd numbers:",sum_odd)
# print("total sum of even numbers:",sum_even)



from countries import countries

# land_list = []

# for country in countries:
#     if "land" in country.lower():
#         land_list.append(country)
# print(land_list)


# fruits = ['banana', 'orange', 'mango', 'lemon']

# reversed_fruits = []

# for i in range(len(fruits)-1, -1, -1):
#     reversed_fruits.append(fruits[i])
# print(reversed_fruits)

import countries_data

languages = set()  # use a set to avoid duplicates

for country in countries_data.countries_data:
    for lang in country['languages']:
        languages.add(lang)

print("Total number of languages:", len(languages))
