def solution(number):
    return sum([num for num in range(number) if num % 3 == 0 or num % 5 == 0])


def main():
    print(solution(10))


if __name__ == '__main__':
    main()

# version #2
# def solution(number):
#     sum = 0
#     for i in range(number):
#         if (i % 3) == 0 or (i % 5) == 0:
#             sum += i
#     return sum
