from zipfile import ZipFile
from pathlib import Path

Path('./Раздел 48 - Работа с zip архивами/my-files').mkdir()

with open ('./Раздел 48 - Работа с zip архивами/my-files/first.txt', 'w') as my_file:
    my_file.write("This is first file")

with open ('./Раздел 48 - Работа с zip архивами/my-files/second.txt', 'w') as my_file:
    my_file.write("This is second file")

with ZipFile("./Раздел 48 - Работа с zip архивами/my-files/my-zip_file", mode='w') as my_zip_file:
    # print(my_zip_file)
    for file in Path('./Раздел 48 - Работа с zip архивами/my-files/').iterdir():
        print(file)
        my_zip_file.write(file)