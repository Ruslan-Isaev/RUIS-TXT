<p>RUIS-TXT or rtxt for short is a library for convenient work with TXT files in Python.</p>
<p>&nbsp;</p>
<p>What are the functions?:</p>
<p>create() - creating a TXT file</p>
<p>write(text) - recording information in TXT</p>
<p>read() - reading a TXT file</p>
<p>clear() - clearing the TXT file</p>
<p>replace(text1, text2) - replacing words in a txt sentence</p>
<p>delete() - deleting a txt file</p>
<p>&nbsp;</p>
<p><strong>Dependencies:</strong></p>
<p>asyncio</p>
<p>aiofiles</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><span style="font-size: medium;"><strong>Getting started</strong></span></p>
<p>&nbsp;</p>
<p>To get started, download the file rtxt.py and put it where it is convenient for you (in this instruction, in order not to suffer, I put the file in the same directory as main.py )</p>
<p>&nbsp;</p>
<p><strong>The import happens like this:</strong></p>
<p>&nbsp;</p>
<p><cite>If you need a synchronous version, then the import looks like this:</cite></p>
<p><cite>from rtxt import Txt File</cite></p>
<p><cite>If you need an asynchronous version, then the import looks like this:</cite></p>
<p><cite>from rtxt import AsyncTxtFile</cite></p>
<p>&nbsp;</p>
<p>If you place the file in a different directory, the import may look different.</p>
<p>&nbsp;</p>
<p><strong>Example of work for the synchronous version:</strong></p>
<p>&nbsp;</p>
<p>#specify the file name or path</p>
<p>filename = 'example.txt'</p>
<p>txt_file = TxtFile(filename)</p>
<p>#Creating a file</p>
<p>txt_file.create()</p>
<p>#Writing text to a file</p>
<p>txt_file.write('Привет, мир!')</p>
<p>#Reading the contents of the file</p>
<p>print(txt_file.read())</p>
<p>#File Cleanup</p>
<p>txt_file.clear()</p>
<p>#Writing a new text</p>
<p>txt_file.write('This is new text!')</p>
<p>#Reading new file contents</p>
<p>print(txt_file.read())</p>
<p>#Text replacement</p>
<p>txt_file.replace('new', 'replace')</p>
<p>#Reading the modified file contents</p>
<p>print(txt_file.read())</p>
<p>#Deleting a file</p>
<p>txt_file.delete()</p>
<p>&nbsp;</p>
<p><strong>An example of how it works for the asynchronous version:</strong></p>
<p>&nbsp;</p>
<p>#specify the file name or path</p>
<p>filename = 'example.txt'</p>
<p>txt_file = AsyncTxtFile(filename)</p>
<p>#Creating a file</p>
<p>await txt_file.create()</p>
<p>#Writing text to a file</p>
<p>await txt_file.write('Hello World!')</p>
<p>#Reading the contents of the file</p>
<p>await txt_file.read()</p>
<p>#File Cleanup</p>
<p>await txt_file.clear()</p>
<p>#Writing a new text</p>
<p>await txt_file.write('This is new text!')</p>
<p>#Reading new file contents</p>
<p>await txt_file.read()</p>
<p>#Text replacement</p>
<p>await txt_file.replace('new', 'replace')</p>
<p>#Reading the modified file contents</p>
<p>await txt_file.read()</p>
<p>#Deleting a file</p>
<p>await txt_file.delete()</p>
<p>&nbsp;</p>
<p>Donate:&nbsp;</p>
<p>СберБанк(Russia) -&nbsp;2202203242397083</p>
<p>Crypto(USDT TRC20), Global -&nbsp;TGhcCz61q5rq6n6GwihozMbuvvT1zCYjVD</p>
<p>&nbsp;</p>
<p>Telegram: @RuisASK</p>
<p>&lt;p&gt;RUIS-TXT или же сокращенно rtxt это библиотека для удобной работы с TXT файлами в Python.&lt;br /&gt;RUIS-TXT or rtxt for short is a library for convenient work with TXT files in Python.&lt;/p&gt;&lt;p&gt;Какие есть функции? / What are the functions?:&lt;br /&gt;create() - создание TXT файла / creating a TXT file&lt;br /&gt;write(text) - запись информации в TXT / recording information in TXT&lt;br /&gt;read() - чтение TXT файла / reading a TXT file&lt;br /&gt;clear() - очистка TXT файла / clearing the TXT file&lt;br /&gt;replace(text1, text2) - замена слов в txt предложении / replacing words in a txt sentence&lt;br /&gt;delete() - удаление txt файла / deleting a txt file&lt;/p&gt;&lt;p&gt;Зависимости / Dependencies:&lt;br /&gt;asyncio&lt;br /&gt;aiofiles&lt;/p&gt;&lt;p&gt;&lt;br /&gt;&amp;lt;h1&amp;gt;Начало работы / Getting started&amp;lt;/h1&amp;gt;&lt;/p&gt;&lt;p&gt;----&lt;/p&gt;&lt;p&gt;Для начала скачайте файл rtxt.py и поместите куда вам удобно(в данной инструкции я чтобы не мучаться поместил файл в тот же каталог, что и main.py)&lt;/p&gt;&lt;p&gt;----&lt;/p&gt;&lt;p&gt;To get started, download the file rtxt.py and put it where it is convenient for you (in this instruction, in order not to suffer, I put the file in the same directory as main.py )&lt;/p&gt;&lt;p&gt;----&lt;/p&gt;&lt;p&gt;Импорт происходит так:&lt;br /&gt;Если вам нужна синхронная версия, то импорт выглядит так:&lt;br /&gt;from rtxt import TxtFile&lt;br /&gt;Если вам нужна асинхронная версия, то импорт выглядит так:&lt;br /&gt;from rtxt import AsyncTxtFile&lt;/p&gt;&lt;p&gt;----&lt;/p&gt;&lt;p&gt;The import happens like this:&lt;br /&gt;If you need a synchronous version, then the import looks like this:&lt;br /&gt;from rtxt import Txt File&lt;br /&gt;If you need an asynchronous version, then the import looks like this:&lt;br /&gt;from rtxt import AsyncTxtFile&lt;/p&gt;&lt;p&gt;----&lt;/p&gt;&lt;p&gt;Если вы разместите файл в другом каталоге, то импорт может выглядеть по другому.&lt;/p&gt;&lt;p&gt;----&lt;/p&gt;&lt;p&gt;If you place the file in a different directory, the import may look different.&lt;/p&gt;&lt;p&gt;----&lt;/p&gt;&lt;p&gt;#Пример работы для синхронной версии/Example of work for the synchronous version:&lt;/p&gt;&lt;p&gt;#указываем имя файла или путь / specify the file name or path&lt;br /&gt;filename = 'example.txt'&lt;br /&gt;txt_file = TxtFile(filename)&lt;br /&gt;# Создание файла / Creating a file&lt;br /&gt;txt_file.create()&lt;br /&gt;# Запись текста в файл / Writing text to a file&lt;br /&gt;txt_file.write('Привет, мир!')&lt;br /&gt;# Чтение содержимого файла / Reading the contents of the file&lt;br /&gt;print(txt_file.read())&lt;br /&gt;# Очистка файла / File Cleanup&lt;br /&gt;txt_file.clear()&lt;br /&gt;# Запись нового текста / Writing a new text&lt;br /&gt;txt_file.write('Это новый текст.')&lt;br /&gt;# Чтение нового содержимого файла / Reading new file contents&lt;br /&gt;print(txt_file.read())&lt;br /&gt;# Замена текста / Text replacement&lt;br /&gt;txt_file.replace('новый', 'замененный')&lt;br /&gt;# Чтение измененного содержимого файла / Reading the modified file contents&lt;br /&gt;print(txt_file.read())&lt;br /&gt;# Удаление файла / Deleting a file&lt;br /&gt;txt_file.delete()&lt;/p&gt;&lt;p&gt;#Пример работы для асинхронной версии / An example of how it works for the asynchronous version:&lt;/p&gt;&lt;p&gt;#указываем имя файла или путь / specify the file name or path&lt;br /&gt;filename = 'example.txt'&lt;br /&gt;txt_file = AsyncTxtFile(filename)&lt;br /&gt;# Создание файла / Creating a file&lt;br /&gt;await txt_file.create()&lt;br /&gt;# Запись текста в файл / Writing text to a file&lt;br /&gt;await txt_file.write('Привет, мир!')&lt;br /&gt;await txt_file.write('Это синхронная запись.')&lt;br /&gt;# Чтение содержимого файла / Reading the contents of the file&lt;br /&gt;await txt_file.read()&lt;br /&gt;# Очистка файла / File Cleanup&lt;br /&gt;await txt_file.clear()&lt;br /&gt;# Запись нового текста / Writing a new text&lt;br /&gt;await txt_file.write('Это новый текст.')&lt;br /&gt;# Чтение нового содержимого файла / Reading new file contents&lt;br /&gt;await txt_file.read()&lt;br /&gt;# Замена текста / Text replacement&lt;br /&gt;await txt_file.replace('новый', 'замененный')&lt;br /&gt;# Чтение измененного содержимого файла / Reading the modified file contents&lt;br /&gt;await txt_file.read()&lt;br /&gt;# Удаление файла / Deleting a file&lt;br /&gt;await txt_file.delete()&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;</p>
