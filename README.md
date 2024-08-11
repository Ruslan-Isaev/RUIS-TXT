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
