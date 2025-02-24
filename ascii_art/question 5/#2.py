from typing import Union
import math

class AsciiArt:
    """A class to generate various ASCII art shapes.

    This class provides methods to create different geometric shapes using ASCII characters.
    All methods include input validation and return formatted multi-line strings.
    """

    @staticmethod
    def _validate_input(dimension: Union[int, float], symbol: str) -> None:
        """Validate input parameters for all drawing methods.

        Args:
            dimension: The size parameter to validate
            symbol: The symbol to validate

        Raises:
            ValueError: If inputs don't meet the requirements
            TypeError: If inputs are of wrong type
        """
        if not isinstance(dimension, (int, float)) or dimension <= 0:
            raise ValueError("Dimensions must be positive numbers")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

    def draw_square(self, width: int, symbol: str) -> str:
        """Draw a square with the specified width and symbol.

        Args:
            width: The width of the square
            symbol: The character to use for drawing

        Returns:
            str: Multi-line string representing the square
        """
        self._validate_input(width, symbol)
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """Draw a rectangle with the specified dimensions and symbol.

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
            symbol: The character to use for drawing

        Returns:
            str: Multi-line string representing the rectangle
        """
        self._validate_input(width, symbol)
        self._validate_input(height, symbol)
        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """Draw an approximate circle with the specified diameter and symbol.

        Args:
            diameter: The diameter of the circle
            symbol: The character to use for drawing

        Returns:
            str: Multi-line string representing the circle
        """
        self._validate_input(diameter, symbol)
        
        radius = diameter / 2
        circle = []
        
        for y in range(diameter):
            line = []
            for x in range(diameter):
                # Calculate if point is within circle using distance formula
                distance = math.sqrt((x - radius + 0.5) ** 2 + (y - radius + 0.5) ** 2)
                line.append(symbol if distance <= radius else ' ')
            circle.append(''.join(line))
        
        return '\n'.join(circle)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """Draw a right-angled triangle with the specified dimensions and symbol.

        Args:
            width: The base width of the triangle
            height: The height of the triangle
            symbol: The character to use for drawing

        Returns:
            str: Multi-line string representing the triangle
        """
        self._validate_input(width, symbol)
        self._validate_input(height, symbol)
        
        triangle = []
        for i in range(height):
            # Calculate symbols for current line based on height ratio
            symbols = int((i + 1) * width / height)
            triangle.append(symbol * symbols)
        
        return '\n'.join(triangle)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """Draw a symmetrical pyramid with the specified height and symbol.

        Args:
            height: The height of the pyramid
            symbol: The character to use for drawing

        Returns:
            str: Multi-line string representing the pyramid
        """
        self._validate_input(height, symbol)
        
        pyramid = []
        for i in range(height):
            # Calculate padding and symbols for current line
            spaces = " " * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            pyramid.append(f"{spaces}{symbols}")
        
        return '\n'.join(pyramid)


def main():
    """Main function to demonstrate the ASCII art functionality."""
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("\nSquare (4x4):")
        print(ascii_art.draw_square(4, "*"))
        
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, "#"))
        
        print("\nCircle (diameter 8):")
        print(ascii_art.draw_circle(8, "@"))
        
        print("\nTriangle (width 5, height 3):")
        print(ascii_art.draw_triangle(5, 3, "+"))
        
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, "$"))

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
