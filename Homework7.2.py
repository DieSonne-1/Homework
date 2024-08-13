import io
from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a', encoding = 'utf-8')
    for i, st in enumerate(strings):
        key = (i+1, file.tell())
        strings_positions[key] = st
        file.write(st + '\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)