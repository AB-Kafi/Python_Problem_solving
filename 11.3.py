import time 

def passedtime(data):
    lasttime = None
    for item in data:
        current = time.time()
        delta = current - (lasttime or current)
        lasttime = time.time()
        yield (delta,item)

for i,j in passedtime("a,b,c,d"):
    print(f"{i:.2} {j}")