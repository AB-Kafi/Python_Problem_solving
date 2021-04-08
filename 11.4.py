class Mychain:
    def __init__(self,*args):
        self.data = args


    def chain(self):
        for i in self.data:
            for j in i:
                yield j


mydata = Mychain('abc',[1,2,3,4])

for i in mydata.chain():
    print(i, end = ' ')
