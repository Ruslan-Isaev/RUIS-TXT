<p>RUIS-TXT или же сокращенно rtxt это библиотека для удобной работы с TXT файлами в Python.<br />RUIS-TXT or rtxt for short is a library for convenient work with TXT files in Python.</p>
<p>Какие есть функции? / What are the functions?:<br />create() - создание TXT файла / creating a TXT file<br />write(text) - запись информации в TXT / recording information in TXT<br />read() - чтение TXT файла / reading a TXT file<br />clear() - очистка TXT файла / clearing the TXT file<br />replace(text1, text2) - замена слов в txt предложении / replacing words in a txt sentence<br />delete() - удаление txt файла / deleting a txt file</p>
<p>Зависимости / Dependencies:<br />asyncio<br />aiofiles</p>
<p><br />Начало работы / Getting started</p>
<p>----</p>
<p>Для начала скачайте файл rtxt.py и поместите куда вам удобно(в данной инструкции я чтобы не мучаться поместил файл в тот же каталог, что и main.py)</p>
<p>----</p>
<p>To get started, download the file rtxt.py and put it where it is convenient for you (in this instruction, in order not to suffer, I put the file in the same directory as main.py )</p>
<p>----</p>
<p>Импорт происходит так:<br />Если вам нужна синхронная версия, то импорт выглядит так:<br />from rtxt import TxtFile<br />Если вам нужна асинхронная версия, то импорт выглядит так:<br />from rtxt import AsyncTxtFile</p>
<p>----</p>
<p>The import happens like this:<br />If you need a synchronous version, then the import looks like this:<br />from rtxt import Txt File<br />If you need an asynchronous version, then the import looks like this:<br />from rtxt import AsyncTxtFile</p>
<p>----</p>
<p>Если вы разместите файл в другом каталоге, то импорт может выглядеть по другому.</p>
<p>----</p>
<p>If you place the file in a different directory, the import may look different.</p>
<p>----</p>
<p>#Пример работы для синхронной версии/Example of work for the synchronous version:</p>
<p>#указываем имя файла или путь / specify the file name or path<br />filename = 'example.txt'<br />txt_file = TxtFile(filename)<br /># Создание файла / Creating a file<br />txt_file.create()<br /># Запись текста в файл / Writing text to a file<br />txt_file.write('Привет, мир!')<br /># Чтение содержимого файла / Reading the contents of the file<br />print(txt_file.read())<br /># Очистка файла / File Cleanup<br />txt_file.clear()<br /># Запись нового текста / Writing a new text<br />txt_file.write('Это новый текст.')<br /># Чтение нового содержимого файла / Reading new file contents<br />print(txt_file.read())<br /># Замена текста / Text replacement<br />txt_file.replace('новый', 'замененный')<br /># Чтение измененного содержимого файла / Reading the modified file contents<br />print(txt_file.read())<br /># Удаление файла / Deleting a file<br />txt_file.delete()</p>
<p>#Пример работы для асинхронной версии / An example of how it works for the asynchronous version:</p>
<p>#указываем имя файла или путь / specify the file name or path<br />filename = 'example.txt'<br />txt_file = AsyncTxtFile(filename)<br /># Создание файла / Creating a file<br />await txt_file.create()<br /># Запись текста в файл / Writing text to a file<br />await txt_file.write('Привет, мир!')<br />await txt_file.write('Это синхронная запись.')<br /># Чтение содержимого файла / Reading the contents of the file<br />await txt_file.read()<br /># Очистка файла / File Cleanup<br />await txt_file.clear()<br /># Запись нового текста / Writing a new text<br />await txt_file.write('Это новый текст.')<br /># Чтение нового содержимого файла / Reading new file contents<br />await txt_file.read()<br /># Замена текста / Text replacement<br />await txt_file.replace('новый', 'замененный')<br /># Чтение измененного содержимого файла / Reading the modified file contents<br />await txt_file.read()<br /># Удаление файла / Deleting a file<br />await txt_file.delete()</p>
<p>&nbsp;</p>
