class Quadrilateral:
    def show(self):
        print("I am a quadrilateral.")

class Parallelogram(Quadrilateral):
    def show(self):
        print("I am a parallelogram.")

shape=Parallelogram()
shape.show()