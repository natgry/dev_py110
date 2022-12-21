import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:
        dict_ = json.load(f)
    # TODO считать содержимое JSON файла

    gen_exr = (elem["contains_improvement_appeals"] for elem in dict_)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
