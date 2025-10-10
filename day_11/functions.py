# def generate_full_name():
#     first_name = "Lakshan"
#     last_name = "Attanayake"

#     full_name = first_name + " " + last_name
#     return full_name

# print(generate_full_name())


# def add_two_numbers():
#     number1 = 3
#     number2 = 5
#     total = number1 + number2
#     return total
# print(add_two_numbers())

# def greetings(name):
#     massege = "Hello "+ name+ ", have a great day!!"
#     return massege
# print(greetings("Lakshan"))

# def square_num(x):
#     return x * x
# print(square_num(100))

# def area_of_circle(r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(3))

# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total += i
#     return total
# print(sum_of_numbers(10))


# def is_even(n):
#     if n % 2 == 0:
#         print("Even")
#         return True
#     return False
# print(is_even(16))


# def add_two_numbers(num1, num2):
#     total = num1 + num2
#     return total

# print(add_two_numbers(4,7))

# def area_of_circle(r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(2))

# def add_all_nums(*args):
#     total = 0
#     for i in args:
#         if not isinstance(i, (int, float)):
#             return f"All arguments must be numbers. '{i}' is not a number."
#         total += i
#     return total
# print(add_all_nums(2, 4, 6, 8))
# print(add_all_nums(2, 4, 6, "9"))


# °F = (°C x 9/5) + 32

# def convert_celsius_to_fahrenheit(c):
#     fahrenheit = (c * 9/5) + 32
#     return fahrenheit
# print(convert_celsius_to_fahrenheit(100))


# def check_season(month):
#     month = month.lower()

#     if month in ("september", "octomber", "November"):
#         return "Autumn"
#     elif month in ("december", "january", "february"):
#         return "Winter"
#     elif month in ("march", "april", "may"):
#         return "Spring"
#     else:
#         return "Summer"
    
# print(check_season("january"))

# def calculate_slope(x1, x2, y1, y2):
#     if x1 == x2:
#         print("slope is undifined!") 
#     slope = y2 - y1/(x2 - x1)
#     return slope
# print(calculate_slope(5, 3, 6, 4))

# import countries_data

# def most_spoken_languages(data, n = 10):
#     language_count = {}

#     for i in countries_data:
#         for language in i["languages"]:
#             if language in language_count:
#                 language_count[language] += 1
#             else:
#                 language_count[language] = 1
from countries_data import countries_data

def most_spoken_languages(counties_data, n=10):
    language_count = {}

    # Loop through all countries in the dataset
    for country in countries_data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    # Sort by how many countries speak each language (descending)
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_languages[:n]
result = most_spoken_languages(countries_data, 5)
print(result)

