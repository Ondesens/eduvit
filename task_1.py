def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

# Тест 1
assert average_num([1, 1]) == 1
# Тест 2
assert average_num([2.5, 3.5]) == 3
# Тест 3
assert average_num([1, 2.5, 3]) == 2.17
# Тест 4
assert average_num(["1", "2", "3"]) == 2
# Тест 5
assert average_num([1, "2", 3.5]) == 2.17
# Тест 6
assert average_num([5]) == 5
# Тест 7
assert average_num([-1, -2, -3]) == -2
# Тест 8
assert average_num([-5, 5, 10]) == 3.33
# Тест 9
assert average_num([1, "abc", 3]) == "Bad request"