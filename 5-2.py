# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    with open('text-2.txt', 'r') as f_open:
        content = f_open.readlines()
        print(f"Количество строк в файле {len(content)}")
        for i, line in enumerate(content):
            print(f"Количечтво слов в {i+1} строке {len(line.split())}")
except IOError:
    print("Произошла ошибка")