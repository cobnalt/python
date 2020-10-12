# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать
# файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
# убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый
# список сохранить в виде json-объекта в соответствующий файл. Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000,
# "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json


def profit(str):
    int_list = list(map(int, str))
    return int_list[0] - int_list[1]


def average_func(dict):
    profit_list = [el for el in dict.values() if el > 0]
    return sum(profit_list)/len(profit_list)


with open('text-7.txt', 'r', encoding='utf-8') as f_open:
    firm_dict = {}
    average = {}
    for line in f_open:
        firm_dict[line.split()[0]] = profit(line.split()[2:])
    average['average_profit'] = average_func(firm_dict)
    common_list = [firm_dict, average]
    with open('text-7.json', 'w') as json_file:
        json.dump(common_list, json_file)
