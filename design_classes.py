# lets design a 2d vector class set

# Think about what data the class will hold
# x , y

# Think about what methods it needs
# init
# str

# Think about what methods could be optional
# add method to add 2 vec2s together
# sub method
# mutiply
# divide

# Draw out diagrams of the class model

# visualize how it will be formed

# write out a basic structure
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def add(self, other):
        self.x += other.x
        self.y += other.y
    
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y

    def mul(self, other):
        self.x *= other.x
        self.y *= other.y

    def div(self, other):
        self.x /= other.x
        self.y /= other.y

    def fdiv(self, other):
        self.x //= other.x
        self.y //= other.y


# reflect on the design & think of improvements

v = Vec2(23, 45)
v2 = Vec2(10, 10)
print(v)
v.add(v2)
print(v)

# Linked Lists to trees

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, value):
        self.left = Node(value)

    def add_right(self, value):
        self.right = Node(value)
