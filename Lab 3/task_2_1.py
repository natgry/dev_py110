import json


def task() -> str:
    dict_numbers = {item: item ** 2 for item in range(1, 11)}  # TODO c помощью dict comprehension сформировать словарь
    return json.dumps(dict_numbers, indent=4)  # TODO сеализовать словарь в JSON строку


if __name__ == "__main__":
    print(task())
