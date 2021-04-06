lis = dict()

while True:
    name = input()
    if  not len(name):
        break
    rain = int(input())
    lis[name] = rain
    
for key,value in lis.items():
    print(key, ':', value)