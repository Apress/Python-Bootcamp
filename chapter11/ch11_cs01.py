class Animal:
    def __init__(self):
        self.type = "unknown"
        self.sound = "unknown"

    def describe(self):
        print(f"Different animals make different sounds.\n")

class Dog(Animal):
    def __init__(self):
        self.type = "domestic"
        self.sound = "barking"
    def describe(self):
        print(f"Dogs are {self.type} animals. ")
        print(f"They prefer {self.sound}.\n")

class Tiger(Animal):
    def __init__(self):
        self.type = "wild"
        self.sound = "roaring"
    def describe(self):
        print(f"Tigers are {self.type} animals. ")
        print(f"They prefer {self.sound}.\n")

animal=Dog()
animal.describe()

animal=Tiger()
animal.describe()