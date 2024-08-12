


import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)

        filetime = os.path.getmtime(file_path)
        formatted_time = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(filetime))


        filesize = str(os.path.getsize(file_path))
        parent_directory = os.path.dirname(file_path)
        with open(os.path.join(parent_directory, 'log.txt'), 'w') as log:
            log.write(formatted_time + ' ' + filesize + '\n')
    print(
            f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_directory}')