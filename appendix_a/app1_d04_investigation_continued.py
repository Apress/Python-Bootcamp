class Color:
  color = "Green"
  def display(self):
     print(f"My favorite color is: {self.color}")

  # @classmethod
  def update_color(cls, newcolor):
     cls.color = newcolor
     print(f"The default color is updated to {newcolor}.")

print(f"The current default is: {Color.color}")
# making an instance of the Color class
color1= Color()
color1.display()
color1.update_color("Blue")
color1.display()
print(f"The current default is: {Color.color}")  # Green now
# print(color1.color)  # Still Blue