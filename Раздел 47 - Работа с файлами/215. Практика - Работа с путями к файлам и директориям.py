from os import path
# print(path.curdir)  # отностительный путь к папке
# print(path.abspath('.'))  # абсолютный путь к папке

from pathlib import Path

# print(type(Path))
# cwd = Path('.')
# cwd = Path('D:/').joinpath('xampp').joinpath('htdocs').joinpath('Python')
cwd = Path('D:/')/'xampp'/'htdocs'/'Python'
cwd_django = Path('D:/')/'xampp'/'htdocs'/'Python' / \
    'Раздел 47 - Работа с файлами'/'django'
# print(cwd.__str__())
# print(cwd)  # current working directory

# print(isinstance(cwd, Path))  # является ли cwd экзепляром класса Path
# print(type(cwd))

# print(Path.__subclasses__())

# print(dir(cwd))  # методы доступные для cwd
"""
['__bytes__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__firstlineno__', '__format__', '__fspath__', '__ge__', '__getattribute__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rtruediv__', '__setattr__', '__sizeof__', '__slots__', 
'__static_attributes__', '__str__', '__subclasshook__', '__truediv__', '_drv', 
'_filter_trailing_slash', '_format_parsed_parts', '_from_parsed_parts', 
'_from_parsed_string', '_glob_selector', '_globber', '_hash', '_max_symlinks',
'_parse_path', '_parts_normcase', '_parts_normcase_cached', '_pattern_str', 
'_raw_path', '_raw_paths', '_remove_leading_dot', '_remove_trailing_slash', 
'_resolving', '_root', '_stack', '_str', '_str_normcase', '_str_normcase_cached',
'_tail', '_tail_cached', '_unsupported_msg', 'absolute', 'anchor', 'as_posix', 
'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', 'from_uri', 'full_match',
'glob', 'group', 'hardlink_to', 'home', 'is_absolute', 'is_block_device', 
'is_char_device', 'is_dir', 'is_fifo', 'is_file', 'is_junction', 'is_mount', 
'is_relative_to', 'is_reserved', 'is_socket', 'is_symlink', 'iterdir', 'joinpath',
'lchmod', 'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent', 'parents', 
'parser', 'parts', 'read_bytes', 'read_text', 'readlink', 'relative_to', 'rename', 
'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 
'suffixes', 'symlink_to', 'touch', 'unlink', 'walk', 'with_name', 'with_segments', 
'with_stem', 'with_suffix', 'write_bytes', 'write_text']
"""

# print(cwd.absolute())
# True - папка присутствует
# print('cwd.absolute().exists() - ', cwd.absolute().exists())

# создание папки с проверкой

if not cwd_django.exists():
    print(cwd_django.mkdir())  # создание папки django
else:
    print('--The folder is exists--')


if cwd_django.exists():
    cwd_django.rmdir()
    print("folder is del")  # удаление папки если она существует

print(Path('.').cwd())
print(type(Path('.')))