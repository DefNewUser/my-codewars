# Если список из чётных, то должен вернуть одну не чётную и наоборот.
# test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
# test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
# test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)


def find_outlier(integers):
    odd = list(filter(lambda x: x % 2 == 1, integers))
    if len(odd) == 1:
        return odd[0]
    else:
        even = list(filter(lambda x: x % 2 == 0, integers))
        return even[0]


def main():
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, -36]))


if __name__ == '__main__':
    main()

array = [2, 4, 0, 100, 4, 11, 2602, 36]

even = [i for i in array if i % 2 == 0]  # Все   чётные числа из array
odd = [i for i in array if i % 2 == 1]  # Все нечётные числа из array

# Бывод первого елемента из списка, который содержит только один элемент

if len(even) == 1:
    print(even[0])
else:
    print(odd[0])
