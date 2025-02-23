
import math

class AsciiArt:
    """
    A class for generating ASCII art shapes.

    Provides methods to draw:
      - Square: draw_square(width: int, symbol: str) -> str
      - Rectangle: draw_rectangle(width: int, height: int, symbol: str) -> str
      - Circle (approximate): draw_circle(diameter: int, symbol: str) -> str
      - Triangle (right-angled): draw_triangle(width: int, height: int, symbol: str) -> str
      - Pyramid: draw_pyramid(height: int, symbol: str) -> str

    Each method returns a multi-line string representing the ASCII art.
    """

    @staticmethod
    def validate_dimension(*dims: int) -> None:
        """
        Validates that the given dimensions are positive integers.
        
        Raises:
            ValueError: If any dimension is not a positive integer.
        """
        for dim in dims:
            if not isinstance(dim, int) or dim < 1:
                raise ValueError("Dimensions must be positive integers (>= 1).")

    @staticmethod
    def validate_symbol(symbol: str) -> None:
        """
        Validates that the provided symbol is a single non-whitespace printable character.

        Raises:
            ValueError: If symbol is not a single, non-whitespace, printable character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable() or symbol.isspace():
            raise ValueError("Symbol must be a single non-whitespace printable character.")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a completely filled square of given width using the specified symbol.

        Parameters:
            width (int): The width (and height) of the square.
            symbol (str): The character used to draw the square.

        Returns:
            str: A multi-line string representing the square.
        """
        self.validate_dimension(width)
        self.validate_symbol(symbol)
        line = symbol * width
        return "\n".join([line for _ in range(width)])

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a completely filled rectangle using the specified dimensions and symbol.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character used to draw the rectangle.

        Returns:
            str: A multi-line string representing the rectangle.
        """
        self.validate_dimension(width, height)
        self.validate_symbol(symbol)
        line = symbol * width
        return "\n".join([line for _ in range(height)])

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle with the given diameter using the specified symbol.

        The circle is filled completely with the selected symbol by checking each point
        against the circle's equation.

        Parameters:
            diameter (int): The diameter of the circle.
            symbol (str): The character used for the circle.

        Returns:
            str: A multi-line string representing the approximate circle.
        """
        self.validate_dimension(diameter)
        self.validate_symbol(symbol)
        radius = diameter / 2
        result_lines = []
        for y in range(diameter):
            line = ""
            for x in range(diameter):
                # Center the check within each "cell" by adding 0.5.
                if (x - radius + 0.5) ** 2 + (y - radius + 0.5) ** 2 <= radius ** 2:
                    line += symbol
                else:
                    line += " "
            result_lines.append(line)
        return "\n".join(result_lines)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled filled triangle with the provided base width and height.
        The triangle will have the right angle at the bottom left.

        Parameters:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character used for the triangle.

        Returns:
            str: A multi-line string representing the triangle.
        """
        self.validate_dimension(width, height)
        self.validate_symbol(symbol)
        result_lines = []
        for row in range(1, height + 1):
            # Calculate the number of symbols in the current row so that the last row has exactly `width` symbols.
            num_symbols = math.ceil(width * row / height)
            num_symbols = min(num_symbols, width)
            result_lines.append(symbol * num_symbols)
        return "\n".join(result_lines)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical filled pyramid of a given height using the specified symbol.
        The pyramid has a base width of (2 * height - 1).

        Parameters:
            height (int): The height of the pyramid.
            symbol (str): The character used for the pyramid.

        Returns:
            str: A multi-line string representing the pyramid.
        """
        self.validate_dimension(height)
        self.validate_symbol(symbol)
        result_lines = []
        for row in range(1, height + 1):
            num_symbols = 2 * row - 1
            # Create leading spaces to center the pyramid.
            spaces = height - row
            line = " " * spaces + symbol * num_symbols
            result_lines.append(line)
        return "\n".join(result_lines)


def main():
    """
    Entry point for the console-based 2D ASCII ART application.
    
    Users can select the shape they want to draw and provide the relevant parameters.
    The ASCII art is then generated and displayed.
    """
    art = AsciiArt()
    menu = """
Choose a shape to draw:
1. Square
2. Rectangle
3. Circle
4. Right-angled Triangle
5. Pyramid
Q. Quit
"""
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip().lower()
        if choice == 'q':
            print("Exiting the ASCII ART application. Goodbye!")
            break

        try:
            if choice == '1':
                width = int(input("Enter the width of the square: "))
                symbol = input("Enter a single non-whitespace printable symbol: ").strip()
                print("\n" + art.draw_square(width, symbol))
            elif choice == '2':
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter a single non-whitespace printable symbol: ").strip()
                print("\n" + art.draw_rectangle(width, height, symbol))
            elif choice == '3':
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter a single non-whitespace printable symbol: ").strip()
                print("\n" + art.draw_circle(diameter, symbol))
            elif choice == '4':
                width = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter a single non-whitespace printable symbol: ").strip()
                print("\n" + art.draw_triangle(width, height, symbol))
            elif choice == '5':
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter a single non-whitespace printable symbol: ").strip()
                print("\n" + art.draw_pyramid(height, symbol))
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as ve:
            print("Error: ", ve)
        except Exception as ex:
            print("An unexpected error occurred: ", ex)
        print("\n" + "=" * 40 + "\n")


if __name__ == "__main__":
    main()
