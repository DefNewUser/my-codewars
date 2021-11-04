# Задача
# Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность/
# и возвращает список элементов без каких-либо элементов с одинаковым значением рядом друг с другом/
# и с сохранением исходного порядка элементов.
import itertools


def unique_in_order(iterable):
    result = []
    prev = None
    for item in iterable:
        if item != prev:
            result.append(item)
            prev = item
    return result


def unique_in_order2(iterable):
    """
    С помощью группового ключа по умолчанию groupby группирует идентичные последовательные элементы,/
     давая кортежи со значением и группой значений (которые мы здесь игнорируем, нам просто нужен ключ)
    :param iterable:
    :return:
    """
    return [k for k, _ in itertools.groupby(iterable)]


def unique_in_order3(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


# лучшее
def unique_in_order4(iterable):
    result = []
    for i in iterable:
        if i not in result:
            result.append(i)
    return result


print(unique_in_order([1, 3, 2, 3, 3]))
print(unique_in_order('ABBCcAD'))
print(unique_in_order('AAAABBBCCDAABBB'))

print(unique_in_order2([1, 3, 2, 3, 2]))
print(unique_in_order2('ABBCcAD'))
print(unique_in_order2('AAAABBBCCDAABBB'))

print(unique_in_order3([1, 3, 2, 3, 2]))
print(unique_in_order3('ABBCcAD'))
print(unique_in_order3('AAAABBBCCDAABBB'))

print(unique_in_order4([1, 3, 2, 3, 2]))
print(unique_in_order4('ABBCcAD'))
print(unique_in_order4('AAAABBBCCDAABBB'))


