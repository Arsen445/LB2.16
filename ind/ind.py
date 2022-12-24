#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def get_trains(trains):
    """
    Запросить данные о рейсе.
    """
    dist = input("Введите пункт для поезда: ")
    time = int(input("Введите время поезда:  "))
    number = input("Тип поезда: ")

    # Создать словарь.
    rey = {
        'dist': dist,
        'time': time,
        'number': number,
    }

    # Добавить словарь в список.
    trains.append(rey)

    # Отсортировать список в случае необходимости.
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('time', ''))
    return trains


def display_trains(trains):
    """
    Отобразить список рейсов.
    """
    # Проверить, что список работников не пуст.
    if trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,

            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Едет в",
                "№ поезда",
                "Время отпр-ния"
            )
        )
        print(line)

        # Вывести данные о всех рейсах.
        for idx, rey in enumerate(trains, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    rey.get('dist', ''),
                    rey.get('time', ''),
                    rey.get('number', 0)
                )
            )
            print(line)

    else:
        print("Список рейсов пуст.")


def select_trains(trains, selected_num):
    """
    Выбрать рейс с нужным пунктом.
    """
    # Сформировать список работников.
    result = []
    for employee in trains:
        if employee.get('dist') == selected_num:
            result.append(employee)
        else:
            print("Нет рейсов в указаный пункт")

    # Возвратить список выбранных работников.
    return result


def save_trains(file_name, staff):
    """
    Сохранить все рейсы в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_trains(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    """
    Главная функция программы.
    """
    #Список рейсов
    trains = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            trains = get_trains(trains)

        elif command == 'list':
            display_trains(trains)

        elif command.startswith('select '):
            # Разбить команду на части.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый город.
            selected_num = str(parts[1])

            selected = select_trains(trains, selected_num)
            display_trains(selected)

        elif command.startswith("save "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]

            # Сохранить данные в файл с заданным именем.
            save_trains(file_name, trains)

        elif command.startswith("load "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]

            # Сохранить данные в файл с заданным именем.
            trains = load_trains(file_name)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select - запросить поездов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")


if __name__ == '__main__':
    main()