class A():
    def __init__(self):
        print("inside A")

        super().__init__()

class B(A):
    def __init__(self):
        print("inside B")

        super().__init__()

class C():
    def __init__(self):

        print("inside C")
        #super().__init__()

class D(B,C):
    def __init__(self):
        print("inside D")
        super().__init__()

obj = D()
print(D.__mro__)