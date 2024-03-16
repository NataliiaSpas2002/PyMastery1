# Strings
# Task 1

message = 'magnificent'
print(message[2])
print(message[-2])
print(message[0:5])
print(message[0:-2])
print(message[2::2])
print(message[1::2])
print(message[::-1])
print(message[::-2])
print(len(message))

# Task 2

sonnet = 'A woman’s face with nature’s own hand painted,'
word_count = len(sonnet.split())
print(word_count)

# Task 3

# Дана строка. Разрежьте ее на две равные части (если длина строки — четная,
# а если длина строки нечетная, то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

message = 'This is my second Python course.'
midle_index = len(message) // 2
if len(message) % 2 == 1:
    midle_index += 1
print(message[midle_index:] + message[:midle_index])

# Task 4

my_string = 'running away'
word1, word2 = my_string.split()
print(f'{word2} {word1}')

# Task 5

sonnet20 ='With shifting change, as is false women’s fashion:'
part1 = sonnet20.find('h')
part2 = sonnet20.rfind('h')
part_to_remove = sonnet20[part1 : part2 + 1]
new_sonnet20 = sonnet20.replace(part_to_remove, ' ')
print(new_sonnet20)

# Task 6

corrector = '1 - orange, 1 - yellow, 3 - green'
one_corrector = corrector.replace('1', 'one')
print(one_corrector)

# Task 7

# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
string2 = 'The quick brown fox jumps over the lazy dog'
new_string2 = string2[0] + ''.join([char for index, char in enumerate(string2) if index % 3 != 0])
print(new_string2)


# Task 8
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

print(greet('Greg', 'Daniel'))

assert greet('Daniel', 'Daniel') == 'Hello boss'
assert greet('Greg', 'Daniel') == 'Hello guest'
