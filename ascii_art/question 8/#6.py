from typing import Union
import math

class AsciiArt:
    """
    A class for creating ASCII art shapes.
    
    This class provides methods to draw various ASCII shapes using specified symbols.
    All methods validate inputs and return formatted multi-line strings.
    """
    
    @staticmethod
    def _validate_inputs(dimension: Union[int, tuple], symbol: str) -> None:
        """
        Validates input parameters for all drawing methods.
        
        Args:
            dimension: Integer or tuple of integers representing shape dimensions
            symbol: Character to use for drawing
            
        Raises:
            ValueError: If inputs are invalid
        """
        if isinstance(dimension, tuple):
            if not all(isinstance(d, int) and d > 0 for d in dimension):
                raise ValueError("Dimensions must be positive integers")
        elif not isinstance(dimension, int) or dimension <= 0:
            raise ValueError("Dimension must be a positive integer")
            
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square with the specified width using the given symbol.
        
        Args:
            width (int): Width of the square
            symbol (str): Character to use for drawing
            
        Returns:
            str: Multi-line string representing the square
        """
        self._validate_inputs(width, symbol)
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle with the specified dimensions using the given symbol.
        
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            symbol (str): Character to use for drawing
            
        Returns:
            str: Multi-line string representing the rectangle
        """
        self._validate_inputs((width, height), symbol)
        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle with the specified diameter using the given symbol.
        
        Args:
            diameter (int): Diameter of the circle
            symbol (str): Character to use for drawing
            
        Returns:
            str: Multi-line string representing the circle
        """
        self._validate_inputs(diameter, symbol)
        
        radius = diameter // 2
        circle = []
        
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                # Use the circle equation (x²/a² + y²/b² ≤ 1)
                if x*x + y*y <= radius*radius:
                    line.append(symbol)
                else:
                    line.append(' ')
            circle.append(''.join(line))
            
        return '\n'.join(circle)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle with the specified dimensions using the given symbol.
        
        Args:
            width (int): Width of the triangle
            height (int): Height of the triangle
            symbol (str): Character to use for drawing
            
        Returns:
            str: Multi-line string representing the triangle
        """
        self._validate_inputs((width, height), symbol)
        
        triangle = []
        for i in range(height):
            # Calculate symbols for current line based on height ratio
            symbols = math.ceil(width * (i + 1) / height)
            triangle.append(symbol * symbols)
            
        return '\n'.join(triangle)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid with the specified height using the given symbol.
        
        Args:
            height (int): Height of the pyramid
            symbol (str): Character to use for drawing
            
        Returns:
            str: Multi-line string representing the pyramid
        """
        self._validate_inputs(height, symbol)
        
        pyramid = []
        for i in range(height):
            # Calculate padding and symbols for current line
            spaces = ' ' * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            pyramid.append(f"{spaces}{symbols}")
            
        return '\n'.join(pyramid)


def main():
    """
    Main function to demonstrate ASCII art functionality.
    """
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("Square (5x5):")
        print(ascii_art.draw_square(5, '*'))
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, '#'))
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, '@'))
        print("\nTriangle (5x3):")
        print(ascii_art.draw_triangle(5, 3, '+'))
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, '^'))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
