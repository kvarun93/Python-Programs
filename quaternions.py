'''

This is the quaterions.py sample code to get you started.

'''

class quat:
    def __init__(self,*args):
        if len(args)==4:
            ## write code here
        elif len(args) == 1:
            self.a = args[0]
            self.b = 0
            self.c = 0
            self.d = 0
        else:
            raise ValueError('Wrong number of inputs to constructor.')
    def __str__(self):
        ## write code here
    def __add__(self,other):
        if type(other) == quat:
            return quat(self.a+other.a,self.b+other.b,self.c+other.c,self.d+other.d)
        else:
            return self+quat(other)
    def __mul__(self,other):
        ## write code here
    def __rmul__(self,other):
        ## write code here
    def __sub__(self,other):
        ## write code here
    def norm(self):
        ## write code here
    def inv(self):
        ## write code here



x = quat(5)
y = quat(0,4,0,0)
z = quat(1,1,1,1)
print(x)
print(x+y)
print(x-y)
print(2*x)
print(x.inv())
print(x*y)
print(x*z)

''' Sample output:
5+0i+0j+0k
5+4i+0j+0k
5+-4i+0j+0k
10+0i+0j+0k
0.2+0.0i+0.0j+0.0k
0+20i+0j+0k
5+5i+5j+5k
'''
