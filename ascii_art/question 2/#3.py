import math


class AsciiArt:
    """
    A class for generating various ASCII art shapes.
    """

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of the given width filled with the specified symbol.

        Args:
            width (int): The width of the square.
            symbol (str): The character to fill the square with.

        Returns:
            str: A multi-line string representing the ASCII art square.

        Raises:
            ValueError: If width is not positive or symbol is not a single character.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle with the given dimensions filled with the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to fill the rectangle with.

        Returns:
            str: A multi-line string representing the ASCII art rectangle.

        Raises:
            ValueError: If width or height are not positive, or symbol is not a single character.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle with the given diameter filled with the specified symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to fill the circle with.

        Returns:
            str: A multi-line string representing the ASCII art circle.
        Raises:
            ValueError: If diameter is not positive or symbol is not a single character.
        """

        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

        radius = diameter // 2
        circle = ""

        for y in range(-radius, radius + 1):
            line = ""
            for x in range(-radius, radius + 1):
                distance = math.sqrt(x * x + y * y)
                # Adjust the threshold for better visual approximation
                if distance <= radius + 0.5:  
                    line += symbol
                else:
                    line += " "  # Use space for outside the circle
            circle += line + "\n"
        return circle

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle with the given dimensions filled with the specified symbol.

        Args:
            width (int): The width of the triangle's base.
            height (int): The height of the triangle.
            symbol (str): The character to fill the triangle with.

        Returns:
            str: A multi-line string representing the ASCII art triangle.

        Raises:
            ValueError: If width or height are not positive, or symbol is not a single character.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

        triangle = ""
        for row in range(1, height + 1):
          #  Calculate the number of symbols in the current row, proportionally to height.
          num_symbols = int((row / height) * width)
          triangle += (symbol * num_symbols).ljust(width) + "\n"

        return triangle
    
    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid with the specified height filled with the given symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to use for drawing the pyramid.

        Returns:
            str: The ASCII art representation of the pyramid.

        Raises:
            ValueError: If height is not positive or if the symbol is not a single character.
        """

        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")


        pyramid = ""
        for row in range(1, height + 1):
            spaces = " " * (height - row)
            symbols = symbol * (2 * row - 1)
            pyramid += spaces + symbols + spaces + "\n"

        return pyramid
def main():
    """
    Main function to demonstrate the ASCII art drawing functionalities.
    """
    art = AsciiArt()

    # Get shape choice from user
    while True:
        print("Choose a shape to draw:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Pyramid")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice < 1 or choice > 6:
                raise ValueError("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError as e:
            print(f"Error: {e}")
            continue
        if choice == 6:
          break

        # Get symbol choice from user

        symbol = input("Enter the symbol to use for drawing: ")

        try:
            if choice == 1:
                width = int(input("Enter width of the square: "))
                print(art.draw_square(width, symbol))
            elif choice == 2:
                width = int(input("Enter width of the rectangle: "))
                height = int(input("Enter height of the rectangle: "))
                print(art.draw_rectangle(width, height, symbol))
            elif choice == 3:
                diameter = int(input("Enter diameter of the circle: "))
                print(art.draw_circle(diameter, symbol))
            elif choice == 4:
                width = int(input("Enter width of the triangle: "))
                height = int(input("Enter height of the triangle: "))
                print(art.draw_triangle(width, height, symbol))
            elif choice == 5:
                height = int(input("Enter height of the pyramid: "))
                print(art.draw_pyramid(height, symbol))
        except ValueError as e:
          print(f"Error: {e}")
        except Exception as e:
          print("An unexpected error occur")

if __name__ == "__main__":
    main()

