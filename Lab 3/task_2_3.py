import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:
        dict_ = json.load(f)  # TODO считать содержимое JSON файла

    return max(dict_, key=lambda x: x["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
