# Задача
# Переместить нули вконец списка, сохраняя последовательность чисел.


def move_zeros(array):
    """
    Делая ключ простым булевым, sorted разбивает его на вещи, которые являются истинными, /
    за которыми следуют вещи, которые являются ложными, и поскольку это стабильный вид, /
    порядок вещей внутри каждой категории такой же, как и исходный вход.
    :param array:
    :return:
    """
    return sorted(array, key=lambda x: not x)  # Or x == 0


print(move_zeros([1, 3, 2, 0, 0, 0, 3, 6]))

# def move_zeros(array):
#     return sorted(array, key=lambda x: x == 0 and x is not False)


a = [1, 3, 2, 0, 0, 0, 3, 6]

result = [n for n in a if n != 0]
result.extend([0] * a.count(0))
print(result)