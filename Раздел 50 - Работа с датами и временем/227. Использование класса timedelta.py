
from datetime import datetime, timedelta

# ---------------- datetime-------------
my_datetime = datetime(2025, 2, 4, 12, 50, 45)

print(timedelta)
print(my_datetime)
# 2025-02-04 12:50:45

print(my_datetime + timedelta(days=100, hours=2, minutes=120))
# 2025-05-15 16:50:45

print(my_datetime - timedelta(days=100, hours=2, minutes=120))
# 2024-10-27 08:50:45
