from typing import List
import math

class AsciiArt:
    """A class for creating various ASCII art shapes.

    This class provides methods to draw different geometric shapes using ASCII characters.
    All methods validate inputs and return properly formatted multi-line strings.
    """

    @staticmethod
    def _validate_inputs(dimension: int, symbol: str) -> None:
        """
        Validates the input parameters for all drawing methods.

        Args:
            dimension (int): The size parameter of the shape.
            symbol (str): The character to be used for drawing.

        Raises:
            ValueError: If inputs don't meet the requirements.
        """
        if not isinstance(dimension, int):
            raise ValueError("Dimension must be an integer")
        if dimension <= 0:
            raise ValueError("Dimension must be positive")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Creates a square ASCII art shape.

        Args:
            width (int): The width and height of the square.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the square.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(width, symbol)
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Creates a rectangular ASCII art shape.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the rectangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(width, symbol)
        self._validate_inputs(height, symbol)
        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Creates a circular ASCII art shape.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the circle.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(diameter, symbol)
        
        radius = diameter // 2
        circle: List[str] = []
        
        for i in range(-radius, radius + 1):
            line = []
            for j in range(-radius, radius + 1):
                if (i**2 + j**2) <= radius**2:
                    line.append(symbol)
                else:
                    line.append(' ')
            circle.append(''.join(line))
        
        return '\n'.join(circle)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Creates a right-angled triangle ASCII art shape.

        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the triangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(width, symbol)
        self._validate_inputs(height, symbol)
        
        triangle = []
        for i in range(height):
            symbols = math.ceil((i + 1) * (width / height))
            triangle.append(symbol * symbols)
        
        return '\n'.join(triangle)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Creates a pyramid ASCII art shape.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the pyramid.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(height, symbol)
        
        pyramid = []
        for i in range(height):
            spaces = " " * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            pyramid.append(spaces + symbols)
        
        return '\n'.join(pyramid)


def main():
    """
    Main function to demonstrate the ASCII art functionality.
    """
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("Square (4x4, using '#'):")
        print(ascii_art.draw_square(4, '#'))
        print("\nRectangle (5x3, using '*'):")
        print(ascii_art.draw_rectangle(5, 3, '*'))
        print("\nCircle (diameter 7, using '@'):")
        print(ascii_art.draw_circle(7, '@'))
        print("\nTriangle (width 5, height 3, using '$'):")
        print(ascii_art.draw_triangle(5, 3, '$'))
        print("\nPyramid (height 4, using '^'):")
        print(ascii_art.draw_pyramid(4, '^'))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


def test_ascii_art():
    art = AsciiArt()
    
    # Test square
    assert art.draw_square(2, '*') == '**\n**'
    
    # Test rectangle
    assert art.draw_rectangle(2, 3, '#') == '##\n##\n##'
    
    # Test invalid inputs
    try:
        art.draw_square(-1, '*')
        assert False, "Should raise ValueError"
    except ValueError:
        pass
