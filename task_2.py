# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open ("input.csv", mode = 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

        with open(OUTPUT_FILENAME, mode='w') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
