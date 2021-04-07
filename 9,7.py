d = {}
counter = 1
for i in range(ord('a'),(ord('z')+1)):
    d[chr(i)] = counter
    counter+=1
print(d)
