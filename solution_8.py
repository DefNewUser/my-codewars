# Задача
# Преобразование целых чисел в римские цифры

def solution(n):
    NUMERALS = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                5: 'V', 4: 'IV', 1: 'I'}
    roman = ""
    for key in NUMERALS.keys():
        count = int(n / key)
        roman += NUMERALS[key] * count
        n -= key * count
    return roman


print(solution(1994))



