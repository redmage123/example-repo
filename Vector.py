class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: ' + str(self.x) + 'y: ' + str(self.y)

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

# Only this new code will be saved in the commit in deltas
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)

    def some_func(self):
        pass
