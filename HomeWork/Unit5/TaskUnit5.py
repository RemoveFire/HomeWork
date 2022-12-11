import random
from random import randint
from sympy import symbols
from math import prod


def RandomNaturalCoefficient(RandMin, RandMax):
    random_number = randint(RandMin, RandMax)
    return random_number


def KoeffForming(RandMin, RandMax, userNumber):
    koeff = [RandomNaturalCoefficient(RandMin, RandMax) for i in range(userNumber)] + [
        RandomNaturalCoefficient(RandMin, RandMax)]
    x = symbols('x')
    y = sum(map(prod, zip(koeff, [x ** i for i in range(userNumber + 1)])))
    return y


def input_check(enter):
    login = None
    check = True
    while check:
        try:
            login = float(input(f"{enter}"))
            check = False
        except ValueError:
            print("Неверный ввод!")
    return login


def U5Task1():
    print("Решение задачи №1: \n")

    with open('database\singular.txt', 'r', encoding='utf8') as file:
        text = file.readline().split()

    print(f'Исходный текст в файле: {text}')
    find = input("Введите что ищем в файле: ")
    new_text = ' '.join(word for word in text if word.find(find) == -1)
    print(f'Записываем в файл следующее содержимое: {new_text}')
    with open('database\singular_result.txt', 'w') as datafile:
        datafile.writelines(new_text)


def U5Task2():
    print("Решение задачи №2: \n")


def U5Task3():
    print("Решение задачи №3: \n")


def U5Task4():
    print("Решение задачи №4: \n")


def U5Task5():
    print("Решение задачи №5: \n")
