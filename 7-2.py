# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

class Coat:
    def __init__(self, v):
        self.v = v
        self.rate = v / 6.5 + 0.5

    @property
    def size(self):
        return f'Размер пальто {self.v}'


class Suit:
    def __init__(self, h):
        self.rate = 2 * h + 0.3


class Clothes:
    def __init__(self):
        self.cs = []

    def add_coat(self, v):
        self.cs.append(Coat(v))

    def add_suit(self, h):
        self.cs.append(Suit(h))

    def common_rate(self):
        main_rate = 0
        for clothe in self.cs:
            main_rate += clothe.rate
        return round(main_rate, 2)


cl1 = Clothes()
cl1.add_coat(43)
cl1.add_coat(45)
cl1.add_suit(1.8)
cl1.add_suit(1.75)
print(cl1.common_rate())

coat1 = Coat(38)
print(coat1.size)
