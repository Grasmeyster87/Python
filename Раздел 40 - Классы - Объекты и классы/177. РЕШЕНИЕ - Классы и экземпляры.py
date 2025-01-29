
class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, resolution_change):
        self.resolution = resolution_change

    def __str__(self):  # конвертация объекта в строку
        return f"{self.title}.{self.extension}"


my_image = Image('1920x1080', 'My_resolution', 'jpg')

print(my_image.__dict__)

my_image.resize('2560x1440')

print(my_image.__dict__)

print(my_image.resolution)
print(my_image.title)
print(my_image.extension)

second_img = Image('8000x500', "My cat", 'png')

print(second_img)