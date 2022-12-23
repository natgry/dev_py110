OUTPUT_FILE = "output.txt"


def task():
    width = 10
    with open(OUTPUT_FILE, "w") as f:
        for count in range(1, width + 1):
            f.write(f"{'*' * count:>{width}}\n")  # TODO записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
