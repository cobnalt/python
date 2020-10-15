# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля - {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость автомобиля - {self.speed}. Вы превышаете скорость!")
        else:
            print(f"Текущая скорость автомобиля - {self.speed}")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость автомобиля - {self.speed}. Вы превышаете скорость!")
        else:
            print(f"Текущая скорость автомобиля - {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(50, 'белый', 'Golf', False)
print(car1.name)
print(car1.speed)
print(car1.color)
print(car1.is_police)
car1.go()
car1.stop()
car1.turn('налево')
car1.show_speed()
car1.speed = 70
car1.show_speed()

car2 = WorkCar(50, 'синий', 'Reno', False)
print(car2.name)
print(car2.speed)
print(car2.color)
print(car2.is_police)
car2.go()
car2.stop()
car2.turn('направо')
car2.show_speed()
car2.speed = 30
car2.show_speed()

car3 = SportCar(150, 'красный', 'Mustang', False)
print(car3.name)
print(car3.speed)
print(car3.color)
print(car3.is_police)
car3.go()
car3.stop()
car3.turn('прямо')
car3.show_speed()

car4 = PoliceCar(60, 'черный', 'Ford', True)
print(car4.name)
print(car4.speed)
print(car4.color)
print(car4.is_police)
car4.go()
car4.stop()
car4.turn('прямо')
car4.show_speed()
