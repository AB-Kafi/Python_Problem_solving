
dictionary = dict()

for i in range(4):
    key, value = input().split()
    dictionary[key] = value

print(dictionary)
dictionary2 = dict()
for key,value in dictionary.items():
    dictionary2[value] = key

dictionary = dictionary2
print(dictionary)