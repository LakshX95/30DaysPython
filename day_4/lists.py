test = []
foods = ['pizza', 'hamburger', 'hotdog', 'spaghetti']
print(len(foods))

print(foods[0])
print(foods[2])
print(foods[3])

mixed_data_types = ['Kobe', 24, 3.14, True]
print(mixed_data_types)

mixed_data_types.append('test data')
print(mixed_data_types)

foods.extend(mixed_data_types)
print(foods)

print(mixed_data_types)

mixed_data_types.append("python")
mixed_data_types.append("SQL")
mixed_data_types.append("Redux")

full_stack = mixed_data_types
print(full_stack)
