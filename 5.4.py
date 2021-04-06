d1 = {'a' : 1, 'b': 2, 'c' : 3}
d2 = {'a' :2, 'b':2, 'c': 3 }
d3 = dict()
def dictdiff(d1, d2):
    se1 = set(d1.items())
    se2 = set(d2.items())
    return dict(se1^se2)
    
print(dictdiff(d1,d2))