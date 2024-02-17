# Task 1
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает
# словарь, в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

my_list = ['apple', 'banana', 'lemon', 'orange', 'cucumber', 'potato']
my_dict = dict()
for i in range(len(my_list)):
    if not i % 2:
        key = my_list[i]
    else:
        value = my_list[i]
        my_dict[key] = value
print(my_dict)

my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}
print(my_dict)

# Task 2

# pseudocode
#1. Create the dict - key: students name, value: study points
#2. determine the average score sum(value)/ len(dict)
#3. if value > averege_score print key(students name)

my_dict = {'John Smith': 80, 'Meryl Strip': 90, 'Bob Strip': 100, 'Linda Evangelista': 55, 'Pol Makartni': 50, 'Sandra Bullock': 70, 'Julia Roberts': 85}
study_points = list(my_dict.values())
print(study_points)
average_points = sum(study_points)/len(study_points)
print(f"{average_points = :.1f}")
excellent_student = [name for name, points in my_dict.items() if points > average_points]
# excellent_student =[]
# for name, points in my_dict.items():
#     if points > average_points:
#         excellent_student.append(name)
print(excellent_student)

# Task 3
# Напишите программу для подсчета количества
# символов (символьной частоты) во введенной строке.

my_str = "A woman’s face with nature’s own hand painted, Hast thou, the master mistress of my passion;"
my_lower_list = list(my_str.lower())

# my_new_value = []
# for i in my_lower_list:
#     my_new_value.append(my_lower_list.count(i))

my_new_value = [my_lower_list.count(i) for i in my_lower_list]

my_new_dict = {my_lower_list[i]: my_new_value[i] for i in range(0, len(my_lower_list))}
print(my_new_dict)

# Task 4
# Обратный словарь: Напишите функцию, которая инвертирует словарь, меняя местами ключи и значения.
# Если возникают дубликаты значений, сохраните последний обработанный ключ.

original_dict = {'John Smith': 80, 'Meryl Strip': 90, 'Bob Strip': 100, 'Linda Evangelista': 50, 'Pol Makartni': 50, 'Sandra Bullock': 70, 'Julia Roberts': 85}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)

# Task 5
# Разность множеств: Напишите функцию, которая принимает два списка и возвращает элементы,
# которые присутствуют в первом списке, но отсутствуют во втором.
list1 = [1, 5, 10, 18, 55, 20, 30, 40, 50, 60]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]
my_set = set(list1) - set(list2)
print(my_set)






