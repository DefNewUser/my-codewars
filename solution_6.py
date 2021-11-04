# Задача
# [      *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************
# ]

def tower_builder(n_floors):
    for i in range(n_floors):
        result = []
        row = '*' * (2 * i + 1)
        print(row.center(2 * n_floors))
        # print(' ' * (n_floors - i - 1) + '*' * (2 * i + 1))


# print(tower_builder(8))


def tower_builder2(n):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]


# print(tower_builder2(10))

def tower_builder3(n_floors):
    tower = []
    floor = ''

    for f in range(n_floors):
        stars = '*' * (f * 2 + 1)
        spaces = ' ' * (n_floors - f - 1)
        floor += spaces + stars + spaces
        tower.append(floor)

    return tower


print(tower_builder3(10))
