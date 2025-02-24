class AsciiArt:
    """
    A class for generating various ASCII art shapes.
    """

    def draw_square(self, width: int, symbol: str = "*") -> str:
        """
        Draws a square of the given width, filled with the specified symbol.

        Args:
            width: The width (and height) of the square.
            symbol: The character to use for drawing the square (default '*').

        Returns:
            A string representing the ASCII art square.  Returns an empty
            string if input is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            print("Error: Width must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1:
            print("Error: Symbol must be a single character.")
            return ""
        if not symbol.isprintable():
            print("Error: Symbol should be printable")
            return ""

        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square

    def draw_rectangle(self, width: int, height: int, symbol: str = "*") -> str:
        """
        Draws a rectangle of the given width and height, filled with the specified symbol.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            symbol: The character to use for drawing (default '*').

        Returns:
            A string representing the ASCII art rectangle. Returns an empty
            string if input is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            print("Error: Width must be a positive integer.")
            return ""
        if not isinstance(height, int) or height <= 0:
            print("Error: Height must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1:
            print("Error: Symbol must be a single character.")
            return ""
        if not symbol.isprintable():
            print("Error: Symbol should be printable")
            return ""

        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle

    def draw_circle(self, diameter: int, symbol: str = "*") -> str:
        """
        Draws an approximate circle of the given diameter, filled with the specified symbol.

        Args:
            diameter: The diameter of the circle.
            symbol:  The character to use for drawing (default '*').

        Returns:
            A string representing the ASCII art circle.  Returns an empty
            string if input is invalid.
        """
        if not isinstance(diameter, int) or diameter <= 0:
            print("Error: Diameter must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1:
            print("Error: Symbol must be a single character.")
            return ""
        if not symbol.isprintable():
            print("Error: Symbol should be printable")
            return ""

        radius = diameter // 2
        circle = ""
        for y in range(-radius, radius + 1):
            line = ""
            for x in range(-radius, radius + 1):
                distance = (x * x + y * y) ** 0.5
                if radius - 0.5 < distance < radius + 0.5:  # Adjust for thickness and approximation
                    line += symbol
                elif distance <= radius:
                    line += symbol
                else:
                    line += " "  # Use spaces for the background
            circle += line + "\n"
        return circle

    def draw_triangle(self, width: int, height: int, symbol: str = "*") -> str:
        """
        Draws a right-angled triangle, filled with the specified symbol.

        Args:
            width:  The width of the triangle's base.
            height: The height of the triangle.
            symbol: The character to use for drawing (default '*').

        Returns:
            A string representing the ASCII art triangle. Returns an empty
            string if input is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            print("Error: Width must be a positive integer.")
            return ""
        if not isinstance(height, int) or height <= 0:
            print("Error: Height must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1:
            print("Error: Symbol must be a single character.")
            return ""
        if not symbol.isprintable():
            print("Error: Symbol should be printable")
            return ""
            
        triangle = ""
        for row in range(1, height + 1):
          line = ""
          for col in range(1, width + 1):
              if col <= (row * width) / height :
                line += symbol
              else:
                line += " "
          triangle += line + "\n"
        return triangle
    
    def draw_pyramid(self, height: int, symbol: str = "*") -> str:
        """
        Draws a symmetrical pyramid of the given height, filled with the specified symbol.

        Args:
            height: The height of the pyramid.
            symbol:  The character to use for drawing (default '*').

        Returns:
            A string representing the ASCII art pyramid. Returns an empty
            string if input is invalid.
        """
        if not isinstance(height, int) or height <= 0:
            print("Error: Height must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1:
            print("Error: Symbol must be a single character.")
            return ""
        if not symbol.isprintable():
            print("Error: Symbol should be printable")
            return ""

        pyramid = ""
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            stars = symbol * (2 * i - 1)
            pyramid += spaces + stars + spaces + "\n"
        return pyramid


# Example Usage (and basic interactive testing)
if __name__ == "__main__":
    art = AsciiArt()

    while True:
        print("\nChoose a shape to draw (or 'exit' to quit):")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Pyramid")

        choice = input("> ").lower()

        if choice == 'exit':
            break

        if choice in ('1', 'square'):
            try:
                width = int(input("Enter width: "))
                symbol = input("Enter symbol (default '*'): ") or "*"
                print(art.draw_square(width, symbol))
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice in ('2', 'rectangle'):
            try:
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                symbol = input("Enter symbol (default '*'): ") or "*"
                print(art.draw_rectangle(width, height, symbol))
            except ValueError:
                print("Invalid input. Please enter integers.")
        elif choice in ('3', 'circle'):
            try:
                diameter = int(input("Enter diameter: "))
                symbol = input("Enter symbol (default '*'): ") or "*"
                print(art.draw_circle(diameter, symbol))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice in ('4', 'triangle'):
            try:
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                symbol = input("Enter symbol (default '*'): ") or "*"
                print(art.draw_triangle(width, height, symbol))
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice in ('5', 'pyramid'):
            try:
                height = int(input("Enter height: "))
                symbol = input("Enter symbol (default '*'): ") or "*"
                print(art.draw_pyramid(height, symbol))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        else:
            print("Invalid choice.")
