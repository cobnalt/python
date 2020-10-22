# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y}*i'

    def __add__(self, other):
        return f'При сложении ({self}) и ({other}) результат {self.x + other.x} + {self.y + other.y}*i'

    def __mul__(self, other):
        return f'При умножении ({self}) и ({other}) результат {self.x * other.x - self.y * other.y} + {self.x * other.y + other.x * self.y}*i'


c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(2, 5)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)