#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

import jsonschema


def get_train():
    """
    Запросить данные о поезде.
    """
    dist = input("Пункт назначения поезда: ")
    time = int(input("Введите время поезда: "))
    typ = input("Тип поезда: ")

    # Создать словарь.
    return {
        "dist": dist,
        "time": time,
        "typ": typ,
    }


def display_trains(staff):
    """
    Отобразить список поездов.
    """
    # Проверить, что список поездов не пуст.
    if staff:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 20, "-" * 15)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^15} |".format(
                "No", "Пункт назначения", "время поезда", "Тип поезда"
            )
        )
        print(line)

        # Вывести данные о всех самолетах.
        for idx, train in enumerate(staff, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:>15} |".format(
                    idx,
                    train.get("dist", ""),
                    train.get("time", 0),
                    train.get("typ", ""),
                )
            )

        print(line)

    else:
        print("Список поездов пуст")


def select_trains(staff, jet):
    """
    Выбрать поезда с заданным типом.
    """
    # Сформировать список поездов.
    result = [train for train in staff if jet == train.get("typ", "")]

    # Возвратить список выбранных поездов.
    return result


def save_trains(file_name, staff):
    """
    Сохранить все поезда в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_trains(file_name):
    """
    Загрузить все поезда из файла JSON.
    """
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "dist": {"type": "string"},
                    "time": {"type": "integer"},
                    "typ": {"type": "string"},
                },
                "required": ["dist", "time", "typ"],
            }
        ],
    }

    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        loadfile = json.load(fin)
        validator = jsonschema.Draft7Validator(schema)
        try:
            if not validator.validate(loadfile):
                print("Валидация прошла успешно")
        except jsonschema.exceptions.ValidationError:
            print("Ошибка валидации", list(validator.iter_errors(loadfile)))
            exit()
    return loadfile


def main():
    """
    Главная функция программы.
    """
    # Список самолетов.
    trains = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == "exit":
            break

        elif command == "add":
            # Запросить данные о поезде.
            train = get_train()

            # Добавить словарь в список.
            trains.append(train)
            # Отсортировать список в случае необходимости.
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get("dist", ""))

        elif command == "list":
            # Отобразить все поезда.
            display_trains(trains)

        elif command.startswith("select "):
            # Разбить команду на части для выделения пункта назначения.
            part = command.split(" ", maxsplit=1)
            com = part[1]

            # Выбрать поезда заданного типа
            selected = select_trains(trains, com)
            # Отобразить выбранные поезда
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

        elif command == "help":
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <тип> - запросить поезда заданного типа;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
            print("load - загрузить json файл.")
            print("save - сохранить json файл.")
            
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
