from zipfile import ZipFile
from pathlib import Path


def make_file_function():
    Path('./Раздел 48 - Работа с zip архивами/my-files').mkdir()


def write_file():
    with open('./Раздел 48 - Работа с zip архивами/my-files/first.txt', 'w') as my_file:
        my_file.write("This is first file")

    with open('./Раздел 48 - Работа с zip архивами/my-files/second.txt', 'w') as my_file:
        my_file.write("This is second file")


def zip_file_function():
    with ZipFile("./Раздел 48 - Работа с zip архивами/my-files/my-zip_file", mode='w') as my_zip_file:
        print(my_zip_file)
        for file in Path('./Раздел 48 - Работа с zip архивами/my-files/').iterdir():
            print(file)
            my_zip_file.write(file)


def un_zip_f():
    with ZipFile("./Раздел 48 - Работа с zip архивами/my-files/my-zip_file") as my_zip_file:
        Path('./Раздел 48 - Работа с zip архивами/my-files-unziped').mkdir()
        my_zip_file.extractall(
            "./Раздел 48 - Работа с zip архивами/my-files-unziped")

with ZipFile("./Раздел 48 - Работа с zip архивами/my-files/my-zip_file") as my_zip_file:
    print(my_zip_file.infolist())


# make_file_function()
# write_file()
# zip_file_function()
# un_zip_f()
