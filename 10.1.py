class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    
    def __str__(self):
        return f"the Flavor is {self.flavor}"

class Cone:
    def __init__(self):
        self.ls = []

    def add_scoop(self,*args):
        for value in args:
           self.ls.append(value)

    def pf(self):
        for i in self.ls:
            print(i)    

ic1 = Scoop("chocolate")
ic2 = Scoop("vanila")
ic3 = Scoop("mint")
ls = [ic1, ic2, ic3]

cone = Cone()
cone.add_scoop(ic1,ic2,ic3)
cone.pf()