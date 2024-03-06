# Напишите программу на Python для возведения элементов списка в квадрат с
# помощью функции map().
my_string = [3, 4, 5, 8, 3, 1, 5, 2, 3, 4, 2]
print(list(map(lambda num: num ** 2, my_string)))

# Напишите программу на Python для преобразования всех символов в прописные и строчные
# и удаления дублирующихся букв из заданной последовательности.
# Используйте функцию map().
original_list = 'Hello World!'
print(list(map(lambda x: x.lower(), set(original_list))))

# Напишите программу на Python, чтобы сложить два заданных списка
# и найти разницу между ними.
# Используйте функцию map().
first_list = '999'
second_list = '444'
print(list(map(lambda x, y: x + y, first_list, second_list)))
print(list(map(lambda x, y: int(x) - int(y), first_list, second_list)))

# Напишите программу на Python для вычисления квадрата первых N чисел Фибоначчи с помощью
# функции map и создания списка этих чисел.

def fib_list(n):
    fib_numbers = []
    a, b = 0, 1
    for i in range(n):
        fib_numbers.append(a)
        a, b = b, a + b

    return fib_numbers
print(fib_list(8))
print(list(map(lambda x: x ** 2, fib_list(8))))