

# ------------- Чтение файла --------------------
# with open('./Раздел 47 - Работа с файлами/testfolder/test.txt') as test_file:
#     print(test_file.read())

# This is a test file
# Another line in the test file

# with open('./Раздел 47 - Работа с файлами/testfolder/test.txt') as test_file:
#     print('\n', test_file.readlines())

# ['This is a test file\n', 'Another line in the test file']

# ------------------ Запись в файл --------------------------

# открытие файла в режиме записи
# with open('./Раздел 47 - Работа с файлами/testfolder/new.txt', 'w') as new_file:
#     new_file.write(
#         "\n\n-----------------------------------------------------------\nFirst line in the new file")

# with open('./Раздел 47 - Работа с файлами/testfolder/new.txt') as new_file:  # файл врежиме чтения
#     print(new_file.read())

# # append открыли файл врежиме дозаписи
# with open('./Раздел 47 - Работа с файлами/testfolder/new.txt', 'a') as new_file:
#     new_file.write("\nSecond line in the new file\n")

# with open('./Раздел 47 - Работа с файлами/testfolder/new.txt') as new_file:  # файл врежиме чтения
#     print(new_file.read())

from pathlib import Path

if Path('./Раздел 47 - Работа с файлами/testfolder/new.txt').exists():
    print("File is present and deleting")
    print(Path('./Раздел 47 - Работа с файлами/testfolder/new.txt').exists())
    Path('./Раздел 47 - Работа с файлами/testfolder/new.txt').unlink()
    print(Path('./Раздел 47 - Работа с файлами/testfolder/new.txt').exists())
else:
    print("File was deleted")
