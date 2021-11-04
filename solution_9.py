# Задача
# Функция, которая удаляет все значения из списка а,
# которые присутствуют в списке b
# array_diff([1,2,2,2,3],[2]) == [1,3]
from speed_timer import speed_timer


@speed_timer
def array_diff(a, b):
    return [x for x in a if x not in b]


@speed_timer
def array_diff_2(a, b):
    return list(set(a) - set(b))


def main():
    print(array_diff([1, 2, 2, 2, 3], [2]))
    print(array_diff_2([1, 2, 2, 2, 3], [2]))


if __name__ == '__main__':
    main()
