import csv
from pathlib import Path


def make_dir():
    Path('./Раздел 49 - Работа с CSV файлами/test_filder').mkdir()


def make_and_write_files():
    with open('./Раздел 49 - Работа с CSV файлами/test_filder/test.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['user_id', 'user_name', 'comments_qty'])
        writer.writerow([5235, 'Vitaliy', 1352])
        writer.writerow([4428, 'Mike', 246])
        writer.writerow([1684, 'Alice', 73])


def make_and_write_files_with_delimeter():
    with open('./Раздел 49 - Работа с CSV файлами/test_filder/test.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['user_id', 'user_name', 'comments_qty'])
        writer.writerow([5235, 'Vitaliy', 1352])
        writer.writerow([4428, 'Mike', 246])
        writer.writerow([1684, 'Alice', 73])


def read_csv_files():
    with open('./Раздел 49 - Работа с CSV файлами/test_filder/test.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        # print(reader)
        # print(type(reader))

        # for line in reader:
        #     print(line)

        # csv_list = list(reader)

        # print(csv_list)

        for line in reader:
            print(line)

        print(reader.line_num)

        # for line in reader:
        #     print(line)


# make_dir()
# make_and_write_files()
make_and_write_files_with_delimeter()
read_csv_files()
