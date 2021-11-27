import datetime


def logger(function_to_log):
    def wrapper(*args, **kwargs):
        now = str(datetime.datetime.now())
        name = function_to_log.__name__

        returned = function_to_log(*args, **kwargs)

        with open('log.txt', 'a') as logfile:
            logfile.write(f'{now}, function: {name}, args: {args}, kwargs: {kwargs}, return: {returned};\n')
        return returned

    return wrapper


def log_to(path):
    def decor(function_to_log):
        def wrapper(*args, **kwargs):
            now = str(datetime.datetime.now())
            name = function_to_log.__name__

            returned = function_to_log(*args, **kwargs)

            with open(path, 'a') as logfile:
                logfile.write(f'{now}, function: {name}, args: {args}, kwargs: {kwargs}, return: {returned};\n')
            return returned

        return wrapper

    return decor


@logger
def some_func(first, name='name'):
    print('первая функция(с агрументами, возвращает 1)')
    return 1


@logger
def another_func():
    print('вторая функция(ничего не возвращает и без аргументов)')


@log_to(path='other.log')
def some_func_to_log(first, name='name'):
    print('первая функция(с агрументами, возвращает 1)')
    return first, name


some_func(first='tets')
another_func()
some_func_to_log(first='test', name='some_name')
