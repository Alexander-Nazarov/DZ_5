import os

class DirDict:
    def __init__(self, path):
        if os.path.exists(path):
            self._path = path
        else:
            print('Incorrect path')

    def __getitem__(self, key):
        if key in self.dict_files():
            path = self._path + '/' + key
            with open(key, 'r') as f:
                return f.read()
        else:
            raise IndexError(key)

    def __setitem__(self, key, value):
        path = self._path + '/' + key
        if not os.path.exists(path):
            os.makedirs(path)
        with open(key, 'w') as f:
            f.write(value)

    def __len__(self):
        return len(os.listdir(self._path))

    def dict_files(self):
        return os.listdir(self._path)
