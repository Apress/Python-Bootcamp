class Grandfather:
    def __init__(self,grandfather):
        print(f"Grandfather: {grandfather}")

class Father(Grandfather):
    def __init__(self, father, grandfather):
        super().__init__(grandfather)
        print(f"Father: {father}")

class Child(Father):
    def __init__(self,name,father,grandfather):
        super().__init__(father,grandfather)
        print(f"Child: {name}")

jack=Child("Jack","Robert","Smith")