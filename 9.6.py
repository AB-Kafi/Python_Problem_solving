from collections import Counter
lis = []
with open("askanother.txt",'r') as fp:
    for i in fp:
        if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
            x =Counter(i[:-1])
            ls = "aeiou" 
            for j in ls:
                if x[j] == 1:
                    lis.append(i[:-1])
                    break
        

print(lis)
