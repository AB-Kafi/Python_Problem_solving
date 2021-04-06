def flatten(ls):
    data = []
    for i in ls:
        data.extend(i)
    return data

print(flatten([[1,2,3,4],[4,2,3]]))