filename = input()
filename = filename+'.txt'
with open(filename, 'a') as fp:
    fp.write("this is the file")