#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def multiplication():
    """""
    Умножение введённых чисел, пока не будет введён 0
    """""
    print("Введите число: ")
    res = 1
    while True:
        a = int(input())
        if a == 0:
            break
        else:
            res *= a
    print("Результат: ", res)


if __name__ == '__main__':
    multiplication()
