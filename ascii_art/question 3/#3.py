
def draw_square(width: int, symbol: str) -> str:
    """Draws a square of the given width, filled with the specified symbol.

    Args:
        width: The width (and height) of the square. Must be >= 1.
        symbol: The character to use to draw the square.  Must be a single character.

    Returns:
        A multi-line string representing the square, or an error message.
    """
    if not isinstance(width, int) or width < 1:
        return "Error: Width must be an integer greater than 0."
    if not isinstance(symbol, str) or len(symbol) != 1:
        return "Error: Symbol must be a single character."

    square_str = ""
    for _ in range(width):
        square_str += symbol * width + "\n"
    return square_str

def draw_rectangle(width: int, height: int, symbol: str) -> str:
    """Draws a rectangle with the given width and height, filled with the specified symbol.

    Args:
        width: The width of the rectangle. Must be >= 1.
        height: The height of the rectangle. Must be >= 1.
        symbol: The character to use. Must be a single character.

    Returns:
        A multi-line string representing the rectangle, or an error message.
    """
    if not isinstance(width, int) or width < 1:
        return "Error: Width must be an integer greater than 0."
    if not isinstance(height, int) or height < 1:
        return "Error: Height must be an integer greater than 0."
    if not isinstance(symbol, str) or len(symbol) != 1:
        return "Error: Symbol must be a single character."

    rectangle_str = ""
    for _ in range(height):
        rectangle_str += symbol * width + "\n"
    return rectangle_str

def draw_circle(diameter: int, symbol: str) -> str:
    """Draws an approximate circle with the given diameter, filled with the specified symbol.

    Args:
        diameter: The diameter of the circle. Must be >= 1.
        symbol: The character to use. Must be a single character.

    Returns:
        A multi-line string representing the circle, or an error message.
    """
    if not isinstance(diameter, int) or diameter < 1:
        return "Error: Diameter must be an integer greater than 0."
    if not isinstance(symbol, str) or len(symbol) != 1:
        return "Error: Symbol must be a single character."

    radius = diameter / 2
    circle_str = ""
    for y in range(-int(radius), int(radius) + 1):
        line = ""
        for x in range(-int(radius), int(radius) + 1):
            distance = (x**2 + y**2)**0.5
            if radius - 0.5 <= distance <= radius + 0.5:  # Create a ring
                line += symbol
            elif distance < radius - 0.5: # Fill the ring
                line += symbol
            else:
                line += " "  # Use spaces for the background
        circle_str += line + "\n"
    return circle_str

def draw_triangle(width: int, height: int, symbol: str) -> str:
    """Draws a right-angled triangle with the given width and height, filled with the specified symbol.

    Args:
        width:  The width of the triangle's base.
        height: The height of the triangle.
        symbol: The character to use. Must be a single character.

    Returns:
        A multi-line string representing the triangle, or an error message.
    """
    if not isinstance(width, int) or width < 1:
        return "Error: Width must be an integer greater than 0."
    if not isinstance(height, int) or height < 1:
        return "Error: Height must be an integer greater than 0."
    if not isinstance(symbol, str) or len(symbol) != 1:
        return "Error: Symbol must be a single character."
    
    triangle_str = ""
    for row in range(1, height + 1):
        # Calculate the number of symbols for this row based on a linear proportion
        num_symbols = int((row / height) * width)
        if num_symbols == 0:
            num_symbols = 1
        triangle_str += symbol * num_symbols
        triangle_str += "\n"
            
    return triangle_str

def draw_pyramid(height: int, symbol: str) -> str:
    """Draws a symmetrical pyramid with the given height, filled with the specified symbol.

    Args:
        height: The height of the pyramid.  Must be >= 1.
        symbol: The character to use.  Must be a single character.

    Returns:
        A multi-line string representing the pyramid, or an error message.
    """
    if not isinstance(height, int) or height < 1:
        return "Error: Height must be an integer greater than 0."
    if not isinstance(symbol, str) or len(symbol) != 1:
        return "Error: Symbol must be a single character."

    pyramid_str = ""
    for i in range(height):
        spaces = " " * (height - i - 1)
        symbols = symbol * (2 * i + 1)
        pyramid_str += spaces + symbols + "\n"
    return pyramid_str


def main():
    """Main function to demonstrate the ASCII art functions."""

    # Get user input for drawing a shape
    print("Choose a shape to draw:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Pyramid")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return

    symbol = input("Enter the symbol to use: ")
    if len(symbol) != 1:
        print("Invalid symbol. Please enter a single character.")
        return

    if choice == 1:
        try:
            width = int(input("Enter the width of the square: "))
            print(draw_square(width, symbol))
        except ValueError:
            print("Invalid width. Please enter an integer.")
    elif choice == 2:
        try:
            width = int(input("Enter the width of the rectangle: "))
            height = int(input("Enter the height of the rectangle: "))
            print(draw_rectangle(width, height, symbol))
        except ValueError:
            print("Invalid width or height. Please enter integers.")
    elif choice == 3:
        try:
            diameter = int(input("Enter the diameter of the circle: "))
            print(draw_circle(diameter, symbol))
        except ValueError:
            print("Invalid diameter. Please enter an integer.")
    elif choice == 4:
        try:
           width = int(input("Enter the width of the triangle: "))
           height = int(input("Enter the height of the triangle: "))
           print(draw_triangle(width, height, symbol))
        except ValueError:
           print("Invalid width of height. Please enter an integer.")

    elif choice == 5:
        try:
            height = int(input("Enter the height of the pyramid: "))
            print(draw_pyramid(height, symbol))
        except ValueError:
            print("Invalid height. Please enter an integer.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()



    import unittest

    class TestAsciiArt(unittest.TestCase):
        def test_draw_square(self):
            self.assertEqual(draw_square(3, "*"), "***\n***\n***\n")
            self.assertEqual(draw_square(1, "X"), "X\n")
            self.assertEqual(draw_square(0, "X"), "Error: Width must be an integer greater than 0.")
            self.assertEqual(draw_square(3, "XX"), "Error: Symbol must be a single character.")
        # Add tests for other functions similarly
    if __name__ == '__main__':
        unittest.main()

    