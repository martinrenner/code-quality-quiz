
from typing import List
import math

class AsciiArt:
    """
    A class for creating various ASCII art shapes.
    Implements functionality for drawing basic geometric shapes using ASCII characters.
    """

    @staticmethod
    def _validate_input(width: int, height: int, symbol: str) -> None:
        """
        Validates input parameters for all drawing functions.

        :param width: Width of the shape
        :param height: Height of the shape
        :param symbol: Character to draw the shape with
        :raises ValueError: If inputs are invalid
        """
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive integers")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square using the specified symbol.

        :param width: Width and height of the square
        :param symbol: Character to draw the square with
        :return: String representation of the square
        """
        self._validate_input(width, width, symbol)
        rows = [symbol * width for _ in range(width)]
        return '\n'.join(rows)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle using the specified symbol.

        :param width: Width of the rectangle
        :param height: Height of the rectangle
        :param symbol: Character to draw the rectangle with
        :return: String representation of the rectangle
        """
        self._validate_input(width, height, symbol)
        rows = [symbol * width for _ in range(height)]
        return '\n'.join(rows)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using the specified symbol.

        :param diameter: Diameter of the circle
        :param symbol: Character to draw the circle with
        :return: String representation of the circle
        """
        self._validate_input(diameter, diameter, symbol)
        
        radius = diameter / 2
        rows: List[str] = []
        
        for y in range(diameter):
            row = ""
            for x in range(diameter):
                # Calculate if point is within circle using distance formula
                distance = math.sqrt((x - radius + 0.5)**2 + (y - radius + 0.5)**2)
                row += symbol if distance <= radius else " "
            rows.append(row)
            
        return '\n'.join(rows)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle using the specified symbol.

        :param width: Width of the triangle
        :param height: Height of the triangle
        :param symbol: Character to draw the triangle with
        :return: String representation of the triangle
        """
        self._validate_input(width, height, symbol)
        
        rows: List[str] = []
        for i in range(height):
            # Calculate number of symbols for current row
            symbols = math.ceil((i + 1) * (width / height))
            rows.append(symbol * symbols)
            
        return '\n'.join(rows)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid using the specified symbol.

        :param height: Height of the pyramid
        :param symbol: Character to draw the pyramid with
        :return: String representation of the pyramid
        """
        self._validate_input(height * 2 - 1, height, symbol)
        
        rows: List[str] = []
        for i in range(height):
            # Calculate spaces and symbols for current row
            spaces = " " * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            rows.append(spaces + symbols)
            
        return '\n'.join(rows)


def main():
    """
    Main function to demonstrate the ASCII art functionality.
    """
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("Square (4x4):")
        print(ascii_art.draw_square(4, "#"))
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, "*"))
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, "@"))
        print("\nTriangle (5x3):")
        print(ascii_art.draw_triangle(5, 3, "+"))
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, "$"))
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
