# Task 15

def check_simbols(string):
    if string.isalpha():
        return 'The string consists only of letters'
    elif string.isdigit():
        return 'The string consists only of digits.'
    elif string.isalnum():
        return 'The string consists of both letters and digits.'
    else:
        return 'The string contains other characters.'


string1 = 'Sonnet20'
string2 = '12345'
string3 = 'A woman’s face with nature’s own hand painted'
string4 = 'Graham'
print(check_simbols(string1))
print(check_simbols(string2))
print(check_simbols(string3))
print(check_simbols(string4))

# Task 16

first = 'liopping'
second = 'stsh'

print(f'{second[2:]}{first[2:]} {first[0:2]}{second[0:2]}')

result = 'shopping list'

# Task 17

sentence = 'Mary went to the forest to find some cranberries'
new_word = sentence.split()
print(new_word[0])

result = 'Mary'

# Task 19

sentence2 = '   Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty   steeps of the Carpathians    themselves       '
new_sentence2 = sentence2.replace('   ', '')
the_last_one = new_sentence2.replace('  ', ' ')
print(the_last_one[0:-1])

# Task 20

example = 'Events happened very rapidly with Francis Morgan that late spring morning'
print(len(example.split()))

# Task 21

def find_symbol(word, index):
    if 0 <= index < len(word):
       symbol = word[index]
       print(f'The index is: {index}, ASCII Code is: {ord(symbol)}')
    else:
        print('Invalid index')

find_symbol('python', 0)

# Task 22
"""
Напишите программу, которая выводит введенную пользователем строку в верхнем регистре 
для первых n символов.

Входные данные
'It was early on a fine summer's day, near the end of the eighteenth century, when a young man, of genteel appearance,
journeying towards the north-east of Scotland'
36

Выходные данные
'IT WAS EARLY ON A FINE SUMMER'S DAY, near the end of the eighteenth century, when a young man, of genteel appearance,
journeying towards the north-east of Scotland'
"""
enter_string = """It was early on a fine summer's day, near the end of the eighteenth century,
when a young man, of genteel appearance, journeying towards the north-east of Scotland"""
print(enter_string)
def part_of_upper_string(enter_string, index):
    return (enter_string.upper()[0:index] + enter_string[index::])

enter_string = """It was early on a fine summer's day, near the end of the eighteenth century,
when a young man, of genteel appearance, journeying towards the north-east of Scotland"""
print(part_of_upper_string(enter_string, 36))

# Task 23

def count_letters_and_digits(input_string):
    letters_count = 0
    digits_count = 0
    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1

    return letters_count, digits_count
input_string = 'Andromeda, M 31, NGC 224'
letters, digits = count_letters_and_digits(input_string)

print(f'Letters: {letters}')
print(f'Digits: {digits}')




# print(count_letters_and_digits('uy123'))


