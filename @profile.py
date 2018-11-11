from timeit import default_timer as timer
from types import FunctionType

def profile(fo):

        def new_fo():
            if isinstance(fo, FunctionType):
                output(fo)
            else:
                for i in fo.__dict__:
                    if isinstance(fo.__dict__[i], FunctionType):
                        output(fo.__dict__[i], True)
        return new_fo

def output(func, cls = False):
    print(func.__qualname__, 'started')
    t = timer()
    if cls:
        func
    else:
        func()
    delta = timer() - t
    print('{} finished in {} seconds\n'.format(func.__qualname__, delta))

def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]

@profile
def foo():
    pass


@profile
class Bar():
    def __init__(self):
        pass
    def foo():
        pass
    def fooo():
        pass

foo()
Bar()
