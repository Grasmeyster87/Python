class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2])

custom_list.print_list_info()

custom_list.append(7)
custom_list.print_list_info()

# print('\n', custom_list.__dict__)
# print('\n', ExtendedList.__dict__)
# print('\n', list.__dict__)
# print('\n', object.__dict__)

print(list.__subclasses__()) # подклассы класса list
