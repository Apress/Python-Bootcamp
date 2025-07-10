class Father:
    def describe(self):
        print("The father is a employee.")
        #super()
class Mother:
    def describe(self):
        print("The mother is a housewife.")
class Child(Father,Mother):
#class Child(Mother,Father):
    # def describe(self):
    #     print("The child is a student.")
    pass

child=Child()
child.describe()
print(Child.mro())

