RUIS-TXT или же сокращенно rtxt это библиотека для удобной работы с TXT файлами в Python.
RUIS-TXT or rtxt for short is a library for convenient work with TXT files in Python.

Какие есть функции? / What are the functions?:
create() - создание TXT файла / creating a TXT file
write(text) - запись информации в TXT / recording information in TXT
read() - чтение TXT файла / reading a TXT file
clear() - очистка TXT файла / clearing the TXT file
replace(text1, text2) - замена слов в txt предложении / replacing words in a txt sentence
delete() - удаление txt файла / deleting a txt file

Зависимости / Dependencies:
asyncio
aiofiles


<h1>Начало работы / Getting started</h1>

----

Для начала скачайте файл rtxt.py и поместите куда вам удобно(в данной инструкции я чтобы не мучаться поместил файл в тот же каталог, что и main.py)

----

To get started, download the file rtxt.py and put it where it is convenient for you (in this instruction, in order not to suffer, I put the file in the same directory as main.py )

----

Импорт происходит так:
Если вам нужна синхронная версия, то импорт выглядит так:
from rtxt import TxtFile
Если вам нужна асинхронная версия, то импорт выглядит так:
from rtxt import AsyncTxtFile

----

The import happens like this:
If you need a synchronous version, then the import looks like this:
from rtxt import Txt File
If you need an asynchronous version, then the import looks like this:
from rtxt import AsyncTxtFile

----

Если вы разместите файл в другом каталоге, то импорт может выглядеть по другому.

----

If you place the file in a different directory, the import may look different.

----

#Пример работы для синхронной версии/Example of work for the synchronous version:

#указываем имя файла или путь / specify the file name or path
filename = 'example.txt'
txt_file = TxtFile(filename)
# Создание файла / Creating a file
txt_file.create()
# Запись текста в файл / Writing text to a file
txt_file.write('Привет, мир!')
# Чтение содержимого файла / Reading the contents of the file
print(txt_file.read())
# Очистка файла / File Cleanup
txt_file.clear()
# Запись нового текста / Writing a new text
txt_file.write('Это новый текст.')
# Чтение нового содержимого файла / Reading new file contents
print(txt_file.read())
# Замена текста / Text replacement
txt_file.replace('новый', 'замененный')
# Чтение измененного содержимого файла / Reading the modified file contents
print(txt_file.read())
# Удаление файла / Deleting a file
txt_file.delete()

#Пример работы для асинхронной версии / An example of how it works for the asynchronous version:

#указываем имя файла или путь / specify the file name or path
filename = 'example.txt'
txt_file = AsyncTxtFile(filename)
# Создание файла / Creating a file
await txt_file.create()
# Запись текста в файл / Writing text to a file
await txt_file.write('Привет, мир!')
await txt_file.write('Это синхронная запись.')
# Чтение содержимого файла / Reading the contents of the file
await txt_file.read()
# Очистка файла / File Cleanup
await txt_file.clear()
# Запись нового текста / Writing a new text
await txt_file.write('Это новый текст.')
# Чтение нового содержимого файла / Reading new file contents
await txt_file.read()
# Замена текста / Text replacement
await txt_file.replace('новый', 'замененный')
# Чтение измененного содержимого файла / Reading the modified file contents
await txt_file.read()
# Удаление файла / Deleting a file
await txt_file.delete()

