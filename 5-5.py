# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

random_int = []
for i in range(25):
    random_int.append(random.randint(1, 500))
f_open = open('text-5.txt', 'w')
f_open.write(" ".join([str(el) for el in random_int]))
f_open.close()
with open('text-5.txt', 'r') as read_f:
    print(sum(map(int, read_f.read().split())))
