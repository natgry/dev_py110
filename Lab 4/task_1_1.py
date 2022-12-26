import json
import re

BOOKS_FILE = "books.md"
BOOKS_FILE_OUTPUT = "books.json"

BOOK_REGEX = r"\s+(?P<position>\d+).\s+" \
             r"\[(?P<book>.+?)\]" \
             r"\((?P<book_url>.+?)\)" \
             r"\s+by\s+(?P<author>.+?)" \
             r"\s+\((?P<recommended>\d{1,3}\.\d+%)\s+recommended\)" \
             r"\s+!\[.*?\]\((?P<cover_url>.+?)\)" \
             r"\s+\n+\"(?P<description>.+?)\"\s+\[.*?\]\(.*?\)"""  # TODO записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    book_data = list()
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            book_data.append(book.groupdict())
            print(json.dumps(book.groupdict(), indent=4))

    with open(BOOKS_FILE_OUTPUT, "w") as f:
        json_data = sorted(book_data, key=lambda item: int(item["position"]), reverse=True)
        json.dump(json_data, f, indent=4)


if __name__ == '__main__':
    task()
