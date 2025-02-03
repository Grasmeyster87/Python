from pathlib import Path

file_path = Path('test.txt')

# print([m for m in dir(file_path)
#       if not m.startswith('_')])  # вывоод в консоль всех методов кроме магических

# print(Path.cwd())  # абсолютный путь к текущей папке

# ------- Формирование новго пути MAC --------
# from pathlib import Path
# print(Path('usr').joinpath('local').joinpath('bin'))

# print(Path('usr')/'local'/'bin')

# ------- Формирование новго пути MAC --------
# from pathlib import Path
# print(Path('C:/').joinpath('Users').joinpath('Vitaliy'))

# print(Path('C:/')/'Users'/'Vitaliy')


# -------- Проверка присутствия директории или файла на компьютере
# from pathlib import Path

# print(Path('main.py').exists())
# print(Path('C:/Users/Azal').exists())
# print(Path('other.py').exists())


# print(Path('main.py').is_file())

# print(Path('../python').is_file())

# print(Path('Раздел 46 - JSON').is_dir())

# ----------------- Список файлов и папок --------------

# from pathlib import Path

for f in Path('.').iterdir():
    print(f)
