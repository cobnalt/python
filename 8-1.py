# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class MyDate:
    def __init__(self, str_date):
        self.date, self.month, self.year = MyDate.validate_date(str_date)

    def __str__(self):
        return f'Число {self.date}, месяц {self.month}, год {self.year}'

    @classmethod
    def int_date(cls, str_date):
        return [int(el) for el in str_date.split('-') if el]

    @staticmethod
    def validate_date(str_date):
        date, month, year = MyDate.int_date(str_date)
        if date < 1:
            date = 1
        elif date > 31:
            date = 31
        if month < 1:
            month = 1
        elif month > 12:
            month = 12
        if year < 0:
            year = 0
        elif year > 2020:
            year = 2020
        return date, month, year


md = MyDate('-12--02-1987')
print(md)
