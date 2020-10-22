# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class OwnZeroDivExcept(Exception):
    def __init__(self, text):
        self.text = text


inp_data = input("Введите делимое: ")
inp_data1 = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    inp_data1 = int(inp_data1)
    if inp_data1 == 0:
        raise OwnZeroDivExcept("На 0 делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnZeroDivExcept as err:
    print(err)
else:
    print(f"Все хорошо. Результат: {inp_data / inp_data1}")


