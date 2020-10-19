# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __str__(self):
        str_list = ""
        for one_list in self.list_of_list:
            for el in one_list:
                str_list += str(el) + '\t'
            str_list += "\n"
        return str_list

    def __add__(self, other):
        rez = []
        for (a, b) in zip(self.list_of_list, other.list_of_list):
            inner = []
            for (aa, bb) in zip(a, b):
                inner.append(aa + bb)
            rez.append(inner)
        return Matrix(rez)


m1 = Matrix([[3, 5, 3], [5, 13, 3], [3, 7, 8], [15, 5, 5]])
m2 = Matrix([[5, 2, 1], [3, 9, -2], [1, 12, 2], [2, 8, 15]])
print(m1)
print(m2)
print(m1 + m2)
