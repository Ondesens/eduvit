def decorator(func):
    def output(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызвана с аргументами:\n'
              f'Позиционные аргументы: {args} \n'
              f'Именованные аргументы: {kwargs}\n'
              f'Площадь прямоугольника: {result}\n')
    return output
@decorator
def rectangle_area(length, width):
    return length * width

rectangle_area(10, 5)
