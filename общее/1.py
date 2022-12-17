#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def test():
    """""
    Ввод числа и проверка на знак
    """""
    a = int(input("введите число: "))
    if a < 0:
        negative()
    elif a >= 0:
        positive()


def negative():
    """""
    Вывод число отрицательное
    """""
    print("число отрицательное")


def positive():
    """"
    Вывод число положительное
    """""
    print("число положительное")


if __name__ == '__main__':
    test()
