# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open('text-4.txt', 'r', encoding='utf-8') as text_f:
    trans_map = {'One': "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    for line in text_f:
        new_line = line.replace(line.split()[0], trans_map[line.split()[0]])
        write_f = open('text-4-1.txt', 'a', encoding='utf-8')
        write_f.write(new_line)
        write_f.close()