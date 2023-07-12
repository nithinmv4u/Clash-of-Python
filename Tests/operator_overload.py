class marks():
    def __init__(self,phy=0,che=0,mat=0):
        self.phy=phy
        self.che=che
        self.mat=mat
    def __str__(self):
        return f"{self.phy} physics {self.che} chemistry {self.mat} maths"

    def __add__(self, other):
        phy =self.phy + other.phy
        che=self.che + other.che
        mat=self.mat + other.mat
        return marks(phy,che,mat)


arun=marks(10,20,30)
print(arun)
vipin=marks(12,13,14)
print(vipin)
two=arun + vipin
print(two)