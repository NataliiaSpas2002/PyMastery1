# Напишите программу на Python, чтобы найти позицию индекса и значение максимального и минимального значений в
# заданном списке чисел с помощью лямбд.
# Исходный список:
# [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
# Позиция индекса и значение максимального значения указанного списка:
# (5, 89)
# Позиция индекса и значение минимального значения указанного списка:
# (3, 10.11)

my_string1 = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
my_min_value = lambda x: (x.index(min(x)), min(x))
print(my_min_value(my_string1))

my_max_value = lambda x: (x.index(max(x)), max(x))
print(my_max_value(my_string1))

# Напишите программу на языке Python для численной сортировки заданного списка строк
# (чисел) с помощью лямбд.
# Исходный список:
# ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Отсортируйте указанный список строк (чисел) по порядку:
# ['-500', '-12', '0', '4', '7', '12', '45', '100', '200']

my_unsorted_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
my_sorted_list = sorted(my_unsorted_list, key=lambda x: int(x))
print(my_sorted_list)

# Напишите программу на Python для подсчета количества элементов в заданном списке
# с помощью лямбд.
# Исходный список:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Подсчитайте количество вхождений элементов в указанном списке:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}
my_string2 = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
my_index_dict = dict(map(lambda x: (x, my_string2.count(x)), set(my_string2)))
print(my_index_dict)

# Напишите программу на языке Python для удаления определенных слов из заданного
# списка с помощью лямбд.
# Исходный список:
# ['orange', 'red', 'green', 'blue', 'white', 'black'].
# Удалить слова:
# ['orange', 'black'].
# После удаления указанных слов из указанного списка:
# ['red', 'green', 'blue', 'white'].
my_fruits = ['orange', 'red', 'green', 'blue', 'white', 'black']
my_new_fruits = lambda: (my_fruits.remove('orange'), my_fruits.remove('black'))
my_new_fruits()
print(my_fruits)

