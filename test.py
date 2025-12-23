li = 'abc'


def change():
    global li
    li = 'abcdef'


change()
print(li)