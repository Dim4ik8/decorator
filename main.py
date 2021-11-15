import datetime


def logger(function_to_log):

    def wrapper(*args, **kwargs):
        now = str(datetime.datetime.now())
        name = function_to_log.__name__
        returned = function_to_log(*args, **kwargs)

        with open('log.txt', 'a') as logfile:
            logfile.write(f'{now}, function: {name}, args: {args}, kwargs: {kwargs}, return: {returned};\n')

    return wrapper


@logger
def some_func(first, name='name'):
    print('первая функция(с агрументами, возвращает 1)')
    return 1


@logger
def another_func():
    print('вторая функция(ничего не возвращает и без аргументов)')


some_func(first='tets')
another_func()