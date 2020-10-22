# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
# постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по
# ООП.

class Stock:
    def __init__(self):
        self.storage = {}

    def take_equipment(self, equip_name, quantity):
        if equip_name.name in self.storage:
            self.storage[equip_name.name] += quantity
        else:self.storage[equip_name.name] = quantity

    def __str__(self):
        str_eq = 'На складе есть \n'
        for name, quant in self.storage.items():
            str_eq += name + '\t' + str(quant) + '\n'
        return str_eq


class OfficeEquipment:
    def __init__(self, name):
        self.name = name

    @classmethod
    def work(cls):
        print(f'{cls.__name__} работает')


class Printer(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'{self.name}'


class Scanner(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'{self.name}'


class Xerox(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'{self.name}'


p = Printer('принтер')
p.work()
print(p)

s = Scanner('сканер')
s.work()
print(s)

x = Xerox("ксерокс")
x.work()
print(x)

stock = Stock()
stock.take_equipment(p, 4)
stock.take_equipment(s, 3)
stock.take_equipment(p, 2)
stock.take_equipment(x, 5)
print(stock)