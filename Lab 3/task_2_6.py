import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)
    json_data = sorted(json_data, key=lambda item: item["length"])
    return json_data  # TODO отсортировать список словарей


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    filename = "output.json"  # TODO дополнительно записать отсортированный список в JSON файл
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
