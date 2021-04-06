#can't solve it . coldn't understand it
d = {'a':1, 'b':2, 'c':3}


def transform_values(f,d):
    return {key:f(value)
    for key,value in d.items()}

print(transform_values(lambda x: x*x, d))
