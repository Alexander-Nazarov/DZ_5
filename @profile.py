from timeit import default_timer as timer
from types import FunctionType

def profile(fo):

        def new_fo():
            if str(type(fo)) == "<class 'function'>":
                print(fo.__name__, 'started')
                t = timer()
                fo()
                delta = timer() - t
                print('{} finished in {} seconds\n'.format(fo.__name__, delta))
            else:
                for i in methods(fo):
                    r = timer()
                    print(fo.__name__,'.',i, ' started', sep = '')
                    delta = timer() - r
                    print(fo.__name__, '.', i, ' finished in {} seconds\n'.format(delta), sep = '')
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

foo()
Bar()
