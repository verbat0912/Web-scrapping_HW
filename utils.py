from datetime import datetime
from functools import wraps


def logger1(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            start_func = datetime.now()
            name_func = old_function.__name__
            with open('main.log', 'a', encoding='utf-8') as f:
                f.writelines(f'Дата запуска функции: {start_func};\n Имя функции:{name_func};\n '
                             f'Аргументы функции:{[*args]}{dict(**kwargs)}\n Результат: {result}\n')
    return new_function


def logger2(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            start_func = datetime.now()
            name_func = old_function.__name__
            with open(path, 'a', encoding='utf-8') as f:
                f.writelines(f'Дата запуска функции: {start_func};\n Имя функции:{name_func};\n '
                             f'Аргументы функции:{[*args]}{dict(**kwargs)}\n Результат: {result}\n')
            return result
        return new_function
    return __logger
