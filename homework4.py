# Lesson 4
import random
# Task 2
# Напишите программу, которая принимает список чисел и выводит
# только те числа, которые делятся на 3 без остатка.


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_new_numbers = [number for number in my_numbers if number % 3 == 0]
print(my_new_numbers)

my_new_numbers = [number for number in list(range(1, 11)) if number % 3 == 0]
print(my_new_numbers)

# Task 3
# Разработайте программу для работы с текстовыми данными.
# Программа должна принимать строку и выводить её обратно,
# но в обратном порядке слов.
my_string = 'A woman’s face with nature’s own hand painted'
new_list = my_string.split()
new_list.reverse()
my_reversed_string = ' '.join(new_list)
print(my_reversed_string)

# Task 6
# Общий объем продаж. Разработайте программу, которая просит
# пользователя ввести продажи магазина за каждый день недели.
# Суммы должны быть сохранены в списке.
# Примените цикл, чтобы вычислить общий объем продаж за неделю и показать результат.

sales_volume = input('Pleas enter daily sales volume: ')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_sales_volume = []

while sales_volume.lower() != 'end week':
    daily_sales_volume.append(int(sales_volume))
    sales_volume = input('Pleas enter daily sales volume: ')

for day in weekdays:
    print(day, daily_sales_volume[weekdays.index(day)])


total_sales = sum(daily_sales_volume)

print(f'Total weeks sales: {total_sales}')

# Task 7
# Генератор лотерейных чисел. Разработайте программу, которая генерирует семизначную комбинацию лотерейных чисел.
# Программа должна сгенерировать семь случайных чисел,
# каждое в диапазоне от 0 до 9, и присвоить каждое число элементу списка.
lottery_numbers = []
for i in range(7):
    digit = random.randint(1, 10)
    lottery_numbers.append(digit)
print('Lottery_numbers:', lottery_numbers)


# Task 8
# В программе напишите функцию, которая принимает два аргумента: список и число п.
# Допустим, что список содержит числа.
# Функция должна показать все числа в списке, которые больше п.
new_list = [1, 2, 3, 5, 7, 11, 20]
new_number = 7

my_new_list_numbers = [number for number in new_list if number > new_number]
print(my_new_list_numbers)

# Task 9
# Бег на беговой дорожке

print('Training time|\tCalories burned')
print('-----------------------------')
for min in range(10, 31, 5):
    calories = min * 4.2
    print(min, '\t\t\t\t', calories)


# Task 10
# Таблица соответствия между градусами Цельсия и градусами Фаренгейта.

print('Celsius degrees\tFahrenheit degrees')
print('----------------------------------')
for num in range(1,21):
    fahrenheit = (9/5 * num + 32)
    print(num, '\t\t\t\t', format(fahrenheit, '.1f'))