def isEven(value: int) -> bool:
    return str(bin(value))[-1] == '0'
# Можно реализовать проверку четности числа через двоичную систему.
# Однако это не имеет преимущества перед стандартным методом, вследствие чего не используется


def printIsEven(number: int):
    if isEven(number):
        print(f'Число {number} - четное')
    else:
        print(f'Число {number} - нечетное')


def testIsEven():  # Сделаем функцию для тестирования различных предзаданных данных и одно ручного ввода
    printIsEven(2)
    printIsEven(39)
    printIsEven(982)
    printIsEven(10102)
    printIsEven(89123751)
    printIsEven(574823745893274593742593)
    print('Введите число для проверки на четность:', end='')
    printIsEven(int(input()))


testIsEven()
