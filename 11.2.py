class Circle:
    def __init__(self, data, times):
        self.data = data
        self.times = times
        self.index = 0
    
    def __next__(self):
        if self.index >= self.times:
            raise StopIteration
        value = self.data[self.index%len(self.data)]
        self.index += 1
        return value

    def __iter__(self):
        return self
    
myls = Circle("abc", 5)
print(list(myls))