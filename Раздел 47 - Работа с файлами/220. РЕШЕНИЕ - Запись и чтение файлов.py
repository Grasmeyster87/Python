import os

from pathlib import Path

import shutil

text1 = """Уроки Python

Python — это кроссплатформенный высокоуровневый язык программирования с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества. Он используется в машинном обучении, веб-разработке, десктопных приложениях и многих других областях.

К счастью для новичков, Python один из самых простых высокоуровневых языков программирования, который имеет простой и удобный синтаксис. Это делает Python отличным языком для изучения новичками.

Представленные уроки по Python охватывают все основные концепции Python. И к концу вы уже сможете создавать проекты на Python."""

text2 = """
Зачем изучать Python?

   Python прост в освоении. Его синтаксис лаконичный, а код легко читается. Читать и писать программы на Python намного проще, чем на других языках, таких как C++, Java, C#.

   Бесплатный и с открытым исходным кодом. Вы можете свободно использовать и распространять код Python даже в коммерческих целях.

   Python используется для разработки веб-приложений, обработки данных, быстрой разработки приложений (RAD) и не только.

   Python позволяет писать программы с меньшим количеством строк кода, чем большинство других языков программирования.

   Кроссплатформенность — вы можете переносить программы Python с одной платформы на другую и запускать их без каких-либо изменений.

   Сейчас это один из самых популярных языков программирования.
"""

folder = f'./Раздел 47 - Работа с файлами/testfolder/files'

# Создаем директорию
try:
    os.makedirs(folder)
except FileExistsError:
    print('Директория уже существует')


def write_files():
    # Создаем файл и записываем в него текст
    # | (Path('./Раздел 47 - Работа с файлами/testfolder/files/first.txt').exists() IS NOT True)
    if (Path('./Раздел 47 - Работа с файлами/testfolder/files/first.txt').exists() == False) | (Path('./Раздел 47 - Работа с файлами/testfolder/files/first.txt').exists() == False):
        with open(os.path.join(folder, 'first.txt'), 'w', encoding='utf-8') as f:
            f.write(text1)

        with open(os.path.join(folder, 'second.txt'), 'w', encoding='utf-8') as f:
            f.write(text2)
        print("File is write")
    else:
        print("The file has already been written")


def read_files():
    # with open('./Раздел 47 - Работа с файлами/testfolder/files/first.txt') as first_file:
    #     # print(first_file.readlines())
    #     lines = first_file.readlines()
    #     for line in lines:
    #         print(line)

    # with open('./Раздел 47 - Работа с файлами/testfolder/files/second.txt') as second_file:
    #     # print(second_file.readlines())
    #     lines = second_file.readlines()
    #     for line in lines:
    #         print(line)

    # Reading the file with utf-8 encoding and ignoring errors
    with open(os.path.join(folder, 'first.txt'), 'r', encoding='utf-8') as f:  # errors='ignore'
        text11 = f.read()
        print(text11)

    with open(os.path.join(folder, 'second.txt'), 'r', encoding='utf-8') as f1:  # errors='ignore'
        text12 = f1.read()
        print(text12)


def del_folder():
    # if Path(folder).exists():
    #     Path(folder).unlink()
    #     print('Folder is deleting')
    # else:
    #     print('The folder is missing')

    folder_path = Path(folder)
    if folder_path.exists() and folder_path.is_dir():
        try:
            shutil.rmtree(folder_path)
            print('Folder is deleted')
        except PermissionError:
            print('Permission denied: Unable to delete the folder')
        except Exception as e:
             print(f'Error: {e}')
        else:
         print('The folder is missing')


write_files()
read_files()
# del_folder()
