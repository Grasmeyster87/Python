"""
            ВСТРОЕННЫЕ МОДУЛИ ДЛЯ РАБОТЫ С ФАЙЛАМИ

os - является пакетом, который содержит различные модули, 
в том числе path

pathlib - объектно ориентированый подход к работе с файлами
"""

from pathlib import Path
from os import path

print(path.abspath('.'))
print(type(path))


print('\n\n', Path('.').absolute())
print(type(Path))
