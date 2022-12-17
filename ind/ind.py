#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_student():
    """
    Запросить данные о студенте.
    """
    FIO = input('Ваши фамилия и инициалы: ')
    group = input('введите номер своей группы: ')
    grade = int(input('Ваша успеваемость: '))

    # Создать словарь.
    return {
        'FIO': FIO,
        'group': group,
        'grade': grade,
    }


def display_student(staff):
    """
    Добавить словарь в список.
    """
    # Проверить, что список работников не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 20,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^20} | {:^20} | {:^15} |'.format(
                "No",
                "ФИО.",
                "номер группы",
                "успеваемость"
            )
        )
        print(line)

        # Вывести данные о всех сотрудниках.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<20} | {:<20} | {:>15} |'.format(
                    idx,
                    student.get('FIO', ''),
                    student.get('group', 0),
                    student.get('grade', 0)
                )
            )
        print(line)


def find_students(staff):
    """
    Выбрать студентов с успеваемостью 4 и 5.
    """
    result = []
    for hh in staff:
        if (hh.get('grade') == 4) or (hh.get('grade') == 5):
            result.append(hh)
    # Возвратить список выбранных работников
    return result


def main():
    """""
    Главная функция программы
    """""
    # Список работников
    students = []

    # Организовать бесконечный цикл запроса команд
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            student = get_student()
            students.append(student)

            if len(students) > 1:
                students.sort(key=lambda item: item.get('grade', ' '))

        elif command == 'list':
            display_student(students)

        elif command == 'find':
            found = find_students(students)
            display_student(found)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("find - вывод на фамилий и номеров групп студента с оценками 4 и 5 ;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
