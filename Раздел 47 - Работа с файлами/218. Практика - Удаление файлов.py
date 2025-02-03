from pathlib import Path
my_file = Path('./Раздел 47 - Работа с файлами/testfolder/test.txt')

if my_file.exists() is not True:
    with open('./Раздел 47 - Работа с файлами/testfolder/test.txt', 'a') as test_file:
        i = 4
        while i > 0:
            test_file.write('First string\n')
            test_file.write('\n')
            test_file.write('Second string\n')
            test_file.write('Third string\n\n')
            i -= 1

# if my_file.exists():
#     my_file.unlink()
