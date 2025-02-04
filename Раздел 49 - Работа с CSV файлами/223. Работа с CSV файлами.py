import csv
from pathlib import Path

# Path('./Раздел 49 - Работа с CSV файлами/test_filder').mkdir()

with open('./Раздел 49 - Работа с CSV файлами/test_filder/test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5235, 'Vitaliy', 1352])
    writer.writerow([4428, 'Mike', 246])
    writer.writerow([1684, 'Alice', 73])