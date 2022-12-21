INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f1, open(OUTPUT_FILE, "w") as f2:
        f2.writelines(map(str.upper, f1))
        # TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
