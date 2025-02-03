from pathlib import Path

files_dir = Path('./Раздел 47 - Работа с файлами/testfolder/files')
files_dir.mkdir(exist_ok=True)  # игнорирование  ошибки создания папки

first_file = files_dir / 'first.txt'
second_file = files_dir / 'second.txt'

with open(first_file, 'w') as f:
    f.write("First line \n")
    f.write("Second line \n")

with open(second_file, 'w') as f:
    lines = [
        "First line in the second file",
        "Second line in the second file",
        "Last line in the seocnd file"
    ]
    # f.write("First line \n")
    # f.write("Second line \n")

    for line in lines:
        f.write(line + '\n')

with open(first_file) as f:
    print(f.read())

# with open(second_file) as f:  # такой вариант вывода подходит больше для небольших файлов
#     for line in f.readlines():
#         print(line)
with open(second_file) as f:  # построчного вывода больше подходит для больших файлов
    for line in f:
        print(line.strip())
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     # уберает лишние пробелы и пустые строки переходы на пустые строки
    #     print(line.strip())

first_file.unlink()
second_file.unlink()
files_dir.rmdir()
