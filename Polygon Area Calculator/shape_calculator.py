from math import floor

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width) :
        self.width = width

    def set_height(self, height) :
        self.height = height

    def get_area(self) :
        return self.width * self.height
        
    def get_perimeter(self) :
        return 2*self.width + 2*self.height
    
    # NOTE: ** indicates "power of"
    def get_diagonal(self) : 
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    # Returns a string that represents the shape using lines of "*". 
    # If the width or height is larger than 50, this should return the string: "Too big for picture.".
    def get_picture(self) : 
        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
        else :
            # create one iterable line for the polygon
            line = []
            for idx in range(self.width) :
                line.append("*")
            # repeat the iterable line to match the polygon height
            picture = ""
            for idx in range(self.height) :
                picture = picture + "".join(line) + "\n"
            return picture

    # Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
    # Example: a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
    # we shouldn't have to worry about edge cases here because if the shape is larger in either dimension then the final equation will result in zero
    def get_amount_inside(self, shape) : 
        vert_repeats = floor(self.height / shape.height)
        hori_repeats = floor(self.width / shape.width)
        return vert_repeats * hori_repeats

    def __str__(self) :
        return f"Rectangle(width={self.width}, height={self.height})"

# square, a special instance of rectange where each side is equal
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self) :
        return f"Square(side={self.width})"

    def set_width(self, width) :
        self.set_side(width)

    def set_height(self, height) :
        self.set_side(height)
        
    def set_side(self, side) :
        self.height = side
        self.width = side