class A:
    def display(self):
        print("A.display")

class B(A):
    def display(self):
        print("B.display")
        super().display()

class C(A):
    def display(self):
        print("C.display")
        #super().display()

# # For E11.7
# class D(C, B):
#     pass

# For E11.8
class D(B,C):
    pass

d=D()
d.display()
print(D.mro())