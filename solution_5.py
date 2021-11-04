# Задача
# Некоторые числа обладают забавными свойствами. Например:
# 89 -> 8¹ + 9² = 89 * 1
# 695 -> 6² + 9³ + 5⁴ = 1390 = 695 * 2
# 46288 -> 4³ + 6⁴ + 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Дано положительное целое число n, записанное как abcd ... (a, b, c, d ... цифры) и положительное целое число p
# мы хотим найти положительное целое число k, если оно существует, /
# например, сумма цифр n, взятых в последовательные степени p, равна k * n.
# Другими словами:
# Существует ли целое число k, например: (a ^ p + b ^ (p + 1) + c ^ (p + 2) + d ^ (p + 3) + ...) = n * k
# Если это так, мы вернем k, если не вернем -1.
# Примечание: n и p всегда будут строго положительными целыми числами.
from speed_timer import speed_timer


@speed_timer
def dig_pow(n, p):
    value = 0
    for digit in str(n):  # итерируем число в виде строки
        value += int(digit) ** p  # возводим в степень числа и добавляем в переменную, складывая.
        p += 1  # увеличиваем степень +1, повтор цикла.
    for k in range(1, value):  # сумму(value) итерируем в диапазоне от 1 до value
        if value / k == n:  # и если оно делится на число в диапазоне без остатка
            return k  # выводим его
    return -1  # а если нет, то -1


@speed_timer
def dig_pow2(n, p):
    assert n > 0 and p > 0
    digits = (int(i) for i in str(n))
    result = 0
    for x in digits:
        result += x ** p
        p += 1

    if result % n:
        return -1
    else:
        return result // n


def dig_pow3(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
        return s / n if s % n == 0 else -1


def main():
    # print(dig_pow3(46288, 3))
    # print(dig_pow(695, 2))
    # print(dig_pow2(695, 2))
    # print(dig_pow3(695, 2))
    print(dig_pow3(89, 1))
    # print(dig_pow(91, 1))


if __name__ == '__main__':
    main()
