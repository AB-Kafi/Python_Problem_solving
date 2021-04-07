def menu(**kwarg):
    a,b = kwarg
    
    x = kwarg[a]()
    y = kwarg[b]()
    return x+y

def a():
    return 'a'

def b():
    return 'b'

print(menu(a = a, b = b))