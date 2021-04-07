def a():
     return 'A'


def b():
    return "B"

from menu import menu

x = menu(a = a,b =b)
print(x)