class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return "Радиус: {}".format(self.radius)
    def set_radius(self):
        new_radius = int(input("Новый радиус: "))
        self.radius = new_radius
        return "Новый радиус: {}".format(self.radius)
    
edit_circle = Circle(20)
print(edit_circle.get_radius())
print(edit_circle.set_radius())
