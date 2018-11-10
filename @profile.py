from timeit import default_timer as timer
from types import FunctionType

def profile(fo):

        def new_fo():
            if isinstance(fo, FunctionType):
                print(fo.__name__, 'started')
                t = timer()
                fo()
                delta = timer() - t
                print('{} finished in {} seconds\n'.format(fo.__name__, delta))
            else:
                for i in fo.__dict__:
                    if isinstance(fo.__dict__[i], FunctionType):
                        print(fo.__dict__[i].__name__, 'started')
                        t = timer()
                        fo.__dict__[i]
                        delta = timer() - t
                        print('{} finished in {} seconds\n'.format(fo.__dict__[i].__name__, delta))
        return new_fo


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
