"""
The module has a class "FileReader", whicth is intended for
read data from an any file.
"""


class FileReader():
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name, 'r') as f:
                return f.read()
        except IOError:
            return ""


def main():
    reader = FileReader('example.txt')
    print(reader.read())


if __name__ == "__main__":
    main()
