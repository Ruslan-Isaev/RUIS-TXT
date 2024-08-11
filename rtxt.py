import os
import asyncio
import aiofiles

class AsyncTxtFile:
    def __init__(self, filename):
        self.filename = filename

    async def create(self):
        try:
            async with aiofiles.open(self.filename, 'w') as file:
                await file.write('')
            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    async def write(self, text):
        try:
            async with aiofiles.open(self.filename, 'a') as file: 
                await file.write(text + '\n')
            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    async def read(self):
        try:
            async with aiofiles.open(self.filename, 'r') as file:
                content = await file.read()  
            return f'{content}'
        except Exception as e:
            return f'Error: {e}'

    async def clear(self):
        try:
            async with aiofiles.open(self.filename, 'w') as file:  
                await file.write('')  
            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    async def replace(self, text1, text2):
        try:
            async with aiofiles.open(self.filename, 'r') as file:
                content = await file.read()  

            new_content = content.replace(text1, text2)  

            async with aiofiles.open(self.filename, 'w') as file:
                await file.write(new_content)  

            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    async def delete(self):
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
                return f'Successfully'
            else:
                return f'The file "{self.filename}" does not exist'
        except Exception as e:
            return f'Error: {e}'
        
class TxtFile:
    def __init__(self, filename):
        self.filename = filename

    def create(self):
        try:
            with open(self.filename, 'w') as file:
                file.write('')  
            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    def write(self, text):
        try:
            with open(self.filename, 'a') as file:  
                file.write(text + '\n')  
            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()  
            return f'{content}'
        except Exception as e:
            return f'Error: {e}'

    def clear(self):
        try:
            with open(self.filename, 'w') as file: 
                file.write('')  
            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    def replace(self, text1, text2):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()  

            new_content = content.replace(text1, text2)  

            with open(self.filename, 'w') as file:
                file.write(new_content)  

            return f'Successfully'
        except Exception as e:
            return f'Error: {e}'

    def delete(self):
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
                return f'Successfully'
            else:
                return f'The file "{self.filename}" does not exist'
        except Exception as e:
            return f'Error: {e}'

