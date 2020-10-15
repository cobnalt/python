# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return print(f'{self.name} {self.surname}')

    def get_total_income(self):
        return print(f'Доход сотрудника {self.name} {self.surname} с учетом премии'
                     f' составляет {self._income["wage"] + self._income["bonus"]}')


pos1 = Position("Иван", "Петров", "бухгалтер", 25000, 7000)
print(pos1.name)
print(pos1.surname)
print(pos1.position)
pos1.get_full_name()
pos1.get_total_income()

pos2 = Position("Вова", "Сидоров", "админ", 35000, 12000)
print(pos2.name)
print(pos2.surname)
print(pos2.position)
pos2.get_full_name()
pos2.get_total_income()
