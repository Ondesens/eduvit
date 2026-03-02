def multiply(nums: list[str], multiplier_1: int):
    list_multiply = []
    for num in nums:
        list_multiply.append(int(num) * multiplier_1)
    return list_multiply

list_number = input('Введите список чисел через пробел: ').split()
multiplier_input = input('Введите множитель (по умолчанию 2): ')
if multiplier_input.strip() :
    multiplier=int(multiplier_input)
else :
    multiplier=2
# Лямбда-функция
multiply_2 = list(map(lambda x: int(x) * multiplier, list_number))

# Вывод результатов
print(f'Результат (функция): {multiply(list_number, multiplier)}')
print(f'Результат (лямбда-функция): {multiply_2}')