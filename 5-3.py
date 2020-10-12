# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

with open('text-3.txt', 'r', encoding='utf-8') as salary_f:
    content = salary_f.readlines()
    salary_list = []
    for line in content:
        name, salary = line.split()
        salary_list.append(int(salary))
        if int(salary) < 20000:
            print(name)
    print(f"Средняя величина дохода сотрудников составляет {(sum(salary_list)/len(salary_list)):.2f}")