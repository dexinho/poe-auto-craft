def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def clear_file(file_path):
    with open(file_path, "w", encoding="utf-8"):
        pass


def update_file(file_path, value):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(str(value) + ' ')


def write_file(file_path, value):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(value))
