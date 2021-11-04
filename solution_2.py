# Задача
# Учитывая целое число, определите, квадратное ли это число:

def is_square(n):
    if n < 0:
        return False
    else:
        return n**0.5 == int(n**0.5)

print(is_square(-9))