class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}"

class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(width=side, height=side)

    def __str__(self):
        return f"Square {self.width}x{self.height}"

if __name__ == "__main__":
    square = Square(4)
    print(square)
    print("area:", square.area())