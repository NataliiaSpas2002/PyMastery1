# Напишите программу на Python, которая создает список слов и с помощью
# функции фильтрации извлекает слова, содержащие более пяти букв.

my_favourite_fruits = ['apple', 'banana', 'kiwi', 'strawberry', 'orange', 'pear', 'peach']
print(list(filter(lambda x: len(x) > 5, my_favourite_fruits)))

# Напишите функцию Python, которая отфильтровывает элементы из списка строк,
# содержащих определенную подстроку, с помощью функции фильтрации.

sonnet_21 = """
Who heaven itself for ornament doth use
And every fair with his fair doth rehearse,
Making a couplement of proud compare
"""
substring_to_filter = 'fair'
filtered_lines = list(filter(lambda x: substring_to_filter not in x, sonnet_21.split('\n')))
for line in filtered_lines:
    print(line)

# Напишите программу на языке Python, которая отфильтровывает
# даты (в формате "YYYY-MM-DD"),
# находящиеся в будущем, с помощью функции фильтрации.
TODAY = '2024-03-06'
my_dates = ['2025-03-04', '2024-11-20', '2022-02-24', '2024-03-04']
print(list(filter(lambda data: data > TODAY, my_dates)))

# Напишите программу на Python, которая создает список кортежей,
# каждый из которых содержит название города и его население.
# Используйте функцию фильтрации для извлечения городов с
# населением более 2 миллионов человек.
# """
list_capitals = {'Mumbai': 21297000, 'Stockholm': 985000, 'Kyiv': 3017000, 'Oslo': 709000, 'London': 9648000}
print(list(filter(lambda city: city[1] > 2000000, list_capitals.items())))