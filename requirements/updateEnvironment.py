import os

if __name__ == '__main__':
    path = os.path.join('env', 'Scripts', 'activate.bat')
    contents = open(path).read()
    sentinel = 'set PYTHONHOME=\n'
    toInsert = 'set "PYTHONPATH=%PYTHONPATH%;%VIRTUAL_ENV%\\.."\n'

    if contents.find(toInsert) == -1:
        index = contents.find(sentinel) + len(sentinel)
        new = contents[:index] + toInsert + contents[index:]
        open(path, 'wb').write(new)