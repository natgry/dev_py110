def header_footer(func):  # TODO написать декоратор
    def wrapper():
        print("========")
        func()
        print("========")
    return wrapper


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
