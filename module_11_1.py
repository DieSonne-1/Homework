import numpy as np

#NamPy
#создадим 2 массива и объеденим их в 1
a = np.array([[1, 2, 10, 16, 30], [3, 5, 20, 55, 8]])
b = np.random.randint(1, 20, size=(2, 5))
c = a + b
print(c)
#Выводим сумму чисел массива и в каждой оси
print(f'Сумма чисел: {c.sum()}')
print(f'Сумма чисел в столбцах: {c.sum(axis = 0)}')
print(f'Сумма чисел в строках: {c.sum(axis = 1)}')
#Выводим среднее арифметическое массива и в каждой оси
print(f'Среднее арифметическое: {c.mean()}')
print(f'Среднее арифметическое  в столбцах: {c.mean(axis = 0)}')
print(f'Среднее арифметическое в строках: {c.mean(axis = 1)}')
#Выводим максимальное и минимальное значение в массиве
print(f'Max: {c.max()}, Min: {c.min()}')

from PIL import Image
from PIL import ImageGrab, ImageOps
from PIL import Image, ImageFilter
#Pillow

#Откроем картинку, получим её размер, а затем изменим его
image = Image.open("ckt.jpg")
width, height = image.size
print(width, height)
new_image = image.resize((1300, 600))
new_image.show()
#Отразим изображение по горизонтале
new_image1 = ImageOps.mirror(image)
new_image1.show()
#Используем фильтр на изображение
new_image2 = image.filter(ImageFilter.FIND_EDGES)
new_image2.show()
new_image3 = ImageOps.grayscale(image)
new_image3.show()
image.save("new.PNG")
