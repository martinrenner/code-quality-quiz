
from typing import List
import math

class AsciiArt:
    """
    A class for creating various ASCII art shapes.
    Implements drawing functionality for basic geometric shapes.
    """

    @staticmethod
    def validate_input(width: int, height: int, symbol: str) -> None:
        """
        Validates input parameters for ASCII art generation.

        Args:
            width (int): The width of the shape
            height (int): The height of the shape
            symbol (str): The symbol to use for drawing

        Raises:
            ValueError: If inputs are invalid
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("Dimensions must be integers")
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a square with the specified width using the given symbol.

        Args:
            width (int): The width and height of the square
            symbol (str): The symbol to use for drawing

        Returns:
            str: A multi-line string representing the square
        """
        AsciiArt.validate_input(width, width, symbol)
        rows = [symbol * width for _ in range(width)]
        return '\n'.join(rows)

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle with the specified dimensions using the given symbol.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            symbol (str): The symbol to use for drawing

        Returns:
            str: A multi-line string representing the rectangle
        """
        AsciiArt.validate_input(width, height, symbol)
        rows = [symbol * width for _ in range(height)]
        return '\n'.join(rows)

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle with the specified diameter using the given symbol.

        Args:
            diameter (int): The diameter of the circle
            symbol (str): The symbol to use for drawing

        Returns:
            str: A multi-line string representing the circle
        """
        AsciiArt.validate_input(diameter, diameter, symbol)
        radius = diameter // 2
        rows: List[str] = []
        
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                # Use the circle equation (x²/a² + y²/b² ≤ 1)
                if x*x + y*y <= radius*radius:
                    line.append(symbol)
                else:
                    line.append(' ')
            rows.append(''.join(line))
        return '\n'.join(rows)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle with the specified dimensions using the given symbol.

        Args:
            width (int): The width of the triangle
            height (int): The height of the triangle
            symbol (str): The symbol to use for drawing

        Returns:
            str: A multi-line string representing the triangle
        """
        AsciiArt.validate_input(width, height, symbol)
        rows = []
        for i in range(height):
            # Calculate symbols for current row based on height ratio
            symbols = math.ceil((i + 1) * (width / height))
            rows.append(symbol * symbols)
        return '\n'.join(rows)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid with the specified height using the given symbol.

        Args:
            height (int): The height of the pyramid
            symbol (str): The symbol to use for drawing

        Returns:
            str: A multi-line string representing the pyramid
        """
        AsciiArt.validate_input(height, height, symbol)
        rows = []
        width = 2 * height - 1
        
        for i in range(height):
            symbols = 2 * i + 1
            padding = (width - symbols) // 2
            row = ' ' * padding + symbol * symbols + ' ' * padding
            rows.append(row)
        return '\n'.join(rows)


def main():
    """
    Main function to demonstrate the ASCII art functionality.
    """
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("Square (4x4):")
        print(ascii_art.draw_square(4, '#'))
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, '*'))
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, '@'))
        print("\nTriangle (5x3):")
        print(ascii_art.draw_triangle(5, 3, '+'))
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, '$'))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
