from math import sqrt

message = """Добро пожаловать в самую лучшую программу для вычисления
квадратного корня из заданного числа"""


def calculate_square_root(number: float):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float):
    """Сравнивает с нулем."""
    if your_number <= 0:
        return

    root = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа.',
          'Это будет: ', root)


print(message)
calc(25.5)
