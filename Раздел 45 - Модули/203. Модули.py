
import dir_for_import.module_one as module_one
# import module_one  #  если модуль в папке
# from module_one import print_name # импорт только определенных переменных

print(type(module_one))
print(dir(module_one))
print(module_one.print_name)

module_one.print_name('\n\nVitaliy')
