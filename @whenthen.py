#C:\Users\User\Desktop\Python\GitHub\DZ_5\@whenthen.py

class Whenthen_cls:
    def __init__(self, fo):
        self.fo = fo
        self.wh_th = []
        self.counter = None

    def when(self, fo):
        def new_fo():
            if not len(self.wh_th) and self.wh_th[self.counter][th] is None:
                self.wh_th.append({wh: fo, th: None})
                if self.counter is None:
                    self.counter = 0
                else:
                    self.counter += 1
        return new_fo

    def then(self, foo):
        def new_fo():
            if self.wh_th[self.counter][th] is None or len(self.wh_th):
                self.wh_th[self.counter][th] = foo
        return new_fo


def whenthen(fo):
    return Whenthen_cls(fo)

@whenthen
def fract(x):
    return x * fract(x - 1)
@fract.when
def fract(x):
    return x == 0
@fract.then
def fract(x):
    return 1
@fract.when
def fract(x):
    return x > 5
@fract.then
def fract(x):
    return x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * fract(x - 5)
