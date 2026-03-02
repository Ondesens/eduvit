def function_name(search: str , status: bool, *args:any , **kwargs: any):
    '''  Функция обрабатывает переданные аргументы в зависимости от параметра search.
    Функция может работать с позиционными аргументами (*args) или именованными 
    аргументами (**kwargs) и возвращать результат в формате list(список) или str(строка).
    
    Параметры Функции:
      search : str
      Может принимать значение:
        args - работа с позиционными аргументами
        kwargs - работа с именованными аргументами

      status : bool
        Работа с позиционными аргументами args:
          Может принимать только два значения:
            True - возвращает список целочисленных аргументов из args
            False - возвращает строку, объединяющую все аргументы args

      *args : any
        Произвольное количество позиционных аргументов любого типа

      **kwargs : any
        Произвольное количество именованных аргументов любого типа

    Raise:
        Если параметр search не равен "args" или "kwargs" возвращает "ValueError"

    Returns
      list | str :
        Возвращает:
        - При search="args" и status=True: список целых чисел из args
        - При search="args" и status=False: строку со всеми значениями args
        - При search="kwargs": строку с перечислением всех ключей и значений kwargs
        - При некорректном search: ошибку ValueError'''

    result: list = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
print(function_name("args", True, 1, 2, "hello", 3.14, [1,2], 5))
print(function_name("args", False, 1, 2, "hello", 3.14, [1,2]))
print(function_name("kwargs", True, name="John", age=25, city="Moscow"))