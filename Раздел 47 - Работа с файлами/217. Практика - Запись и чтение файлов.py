
# --------------------------- Режим записи файлов -------------------------
# test_file = open('./Раздел 47 - Работа с файлами/testfolder/test.txt', 'w')

# print(test_file)
# print(type(test_file))

# test_file.write('First string\n')
# test_file.write('Second string\n')

# test_file.close()
# --------------------- Альтернативній режим чтения файлов с возможностью автозакрітия файлов------

# with open('./Раздел 47 - Работа с файлами/testfolder/test.txt', 'w') as test_file:
#     test_file.write('First string\n')
#     test_file.write('Second string\n')


# --------------------- Режим чтения файлов -------------------------
# test_file = open('./Раздел 47 - Работа с файлами/testfolder/test.txt')
# print(test_file.read())
# test_file.close()

# with open('./Раздел 47 - Работа с файлами/testfolder/test.txt') as test_file:
#     print(test_file.read())

# -------------------- Режим добавления файлов ------------------------
# with open('./Раздел 47 - Работа с файлами/testfolder/test.txt', 'a') as test_file:
#     test_file.write('\n\nFirst string\n')
#     test_file.write('Second string\n')

# with open('./Раздел 47 - Работа с файлами/testfolder/test.txt',) as test_file:
#     print(test_file.read())

# -------------------- Чтение в режиме итерации ---------------------------------

with open('./Раздел 47 - Работа с файлами/testfolder/test.txt', 'a') as test_file:
    test_file.write('First string\n')
    test_file.write('\n')
    test_file.write('Second string\n')
    test_file.write('Third string\n')

with open('./Раздел 47 - Работа с файлами/testfolder/test.txt', 'r') as test_file:
    # print(test_file.readlines())  # ['\n', 'First string\n', 'Second string\n']
    # lines = test_file.readlines()
    # работает одновременно только одна функция  readlines readline
    # line1 = test_file.readline()
    # print(line1)

    # for line in lines:
    #     print(line)

    # for line in test_file:
    #     print(line)

    # print(test_file.readline())
    # print(test_file.readline())
    # print(test_file.readline())
    # res = test_file.readline()

    # print(res)

    # print(type(res))
    # print(res == '')

    while True:
        line = test_file.readline()
        if not line:
            break
        print(line)