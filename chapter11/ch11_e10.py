class A:
    a=1
    _b=2
    __c=3
    __d_=4
    __e__=5

object1=A()
print(object1.a) # Outputs 1
print(object1._b) # Outputs 2
# print(object1.__c) # Error
print(object1._A__c) # Outputs 3
# print(object1.__d_) # Error
print(object1._A__d_) # Outputs 4
print(object1.__e__) # Outputs 5

