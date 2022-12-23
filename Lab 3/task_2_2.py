import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename) as file_input, \
            open(output_filename, "w") as file_output:
        data = json.load(file_input)  # TODO считать содержимое json файл input.json
        json.dump(data, file_output, indent=4)  # TODO записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
