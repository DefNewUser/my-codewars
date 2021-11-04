# Задача
# функция, которая разбивала camel casing, используя пробел между словами.
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
# solution("camelCasing")  ==  "camel Casing"


def solution(s):
    return "".join([" " + i if i.isupper() else i for i in s])


def solution2(s):
    st = ""

    for c in s:
        if c.upper() == c:
            st += " " + c
        else:
            st += c

    return st


def main():
    print(solution('HelloWorld'))
    print(solution2('HelloWorldAndPython'))


if __name__ == '__main__':
    main()