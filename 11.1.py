class Myenumerate(object):
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.index,self.data[self.index]
        self.index +=1
        return value

    def __iter__(self):
        return self

for index,data in Myenumerate("abc"):
    print(index, data)
