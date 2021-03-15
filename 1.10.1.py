# Создайте класс любых геометрических фигур (например, прямоугольник), где на выход получаем характеристики фигуры.
# Каждый экземпляр должен иметь атрибуты x, y, width и height (зависит от выбранной фигуры).
# Вы должны иметь возможность передавать атрибуты при создании, например, для прямоугольника, следующим образом
# (где x = 5, y = 10, width = 50, height = 100 в этом порядке).
# Создайте метод, который возвращает прямоугольник как строку (подсказка: реализация str).
# Для объекта прямоугольника со значениями атрибута x = 5, y = 10, width = 50, height = 100,
# метод должен вернуть строку Rectangle (5, 10, 50, 100).

class Rectangle:

    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def attrib_set(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        return (f'Rectangle ({self.x}, {self.y}, {self.width}, {self.height})')

rectangle = Rectangle()
print(rectangle.attrib_set(5, 10, 50, 100))



