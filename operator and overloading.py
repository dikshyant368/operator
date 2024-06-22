class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x + other.x, self .y + other.y)
    
    def __sub__(self,other):
        return Vector(self.x -other.x, self.y - other.y)
    
    def __mul__(self,other):
        return Vector(self.x * scalar.x, self.y * scalar)
    
    def __str__(self,other): 
        return f"Vector:({self.x},{self.y})"
        
        
    