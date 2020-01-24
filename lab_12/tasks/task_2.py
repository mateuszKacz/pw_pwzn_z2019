from datetime import datetime
from functools import wraps
from time import time


def log_run(fun):
    
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start = time()
        ret = fun(*args, **kwargs)
        end = time()
        fun_time = end - start
        print(datetime.now().strftime('%Y-%m-%dT%H:%M:%S|') + ' function ' + str(fun.__name__) + ' called with:')
        count_pos_params = len(args)
        count_opt_args = len(kwargs)

        print(f'{count_pos_params} positional parameters')
        if count_opt_args > 0:
            opts = ''
            keys = kwargs.keys()
            for key in keys:
                opts += key + ' '
            print(f'optional parameters: {opts}')
        else:
            print(f'optional parameters: -')

        print(f'returned: {ret} ({fun_time}s)')
        return ret
    return wrapper
    pass


@log_run
def fun(*args, **kwargs):
    pass


if __name__ == '__main__':
    decorated_sum = log_run(sum)
    decorated_sum([1,2,3])
    fun(1, 2, 'a', bb=1)
    # Przykładowy log
    # 2020-01-23T21:09:55| function sum called with:
    # 1 postional parameters
    # optional parameters: -
    # returned: 6 (1.43e-06s)
    # 2020-01-23T21:09:55| function fun called with:
    # 3 postional parameters
    # optional parameters: bb
    # returned: None (1.43e-06s)
