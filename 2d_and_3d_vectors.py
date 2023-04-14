class C2d:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def __str__(self):
        return (f'{self.i}i + {self.j}j')

class C3d(C2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    
    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")

a=C2d(2,3)
b=C3d(2,3,4)
print(a)
print(b)