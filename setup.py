from setuptools import setup, find_packages

setup(
    name='rtxt',  # Название вашего пакета
    version='0.1.0',          # Версия вашего пакета
    author='RUIS',       # Ваше имя
    author_email='isaev2k7@gmail.com',  # Ваш email
    description='Library for convenient work with text files',  # Краткое описание
    long_description=open('README.md').read(),  # Длинное описание (обычно из README)
    long_description_content_type='text/html',  # Тип содержимого длинного описания
    url='https://github.com/Ruslan-Isaev/RUIS-TXT',  # URL к репозиторию
    packages=find_packages(),  # Автоматически находит пакеты
    classifiers=[              # Классификаторы для PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Минимальная версия Python
    install_requires=[         # Зависимости вашего пакета
        'asyncio',            # Пример зависимости
        'aiofiles',
    ],
)
