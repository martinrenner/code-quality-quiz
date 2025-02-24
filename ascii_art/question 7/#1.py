
from typing import Union
import math

class AsciiArt:
    """A class for generating various ASCII art shapes.
    
    This class provides methods to create different geometric shapes using ASCII characters.
    All methods validate inputs and return formatted multi-line strings.
    """
    
    @staticmethod
    def _validate_inputs(dimensions: Union[tuple[int, ...], int], symbol: str) -> None:
        """Validates input parameters for all drawing methods.
        
        Args:
            dimensions: Integer or tuple of integers representing shape dimensions
            symbol: Character to use for drawing
            
        Raises:
            ValueError: If dimensions are negative or symbol is empty/multi-character
        """
        if isinstance(dimensions, tuple):
            if any(d <= 0 for d in dimensions):
                raise ValueError("Dimensions must be positive integers")
        elif dimensions <= 0:
            raise ValueError("Dimensions must be positive integers")
            
        if len(symbol) != 1:
            raise ValueError("Symbol must be exactly one character")

    def draw_square(self, width: int, symbol: str) -> str:
        """Draws a square with the specified width using the given symbol.
        
        Args:
            width: Width and height of the square
            symbol: Character to use for drawing
            
        Returns:
            Multi-line string representing the square
        """
        self._validate_inputs(width, symbol)
        rows = [symbol * width for _ in range(width)]
        return '\n'.join(rows)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a rectangle with the specified dimensions using the given symbol.
        
        Args:
            width: Width of the rectangle
            height: Height of the rectangle
            symbol: Character to use for drawing
            
        Returns:
            Multi-line string representing the rectangle
        """
        self._validate_inputs((width, height), symbol)
        rows = [symbol * width for _ in range(height)]
        return '\n'.join(rows)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """Draws an approximate circle with the specified diameter using the given symbol.
        
        Args:
            diameter: Diameter of the circle
            symbol: Character to use for drawing
            
        Returns:
            Multi-line string representing the circle
        """
        self._validate_inputs(diameter, symbol)
        radius = diameter // 2
        rows = []
        
        for y in range(-radius, radius + 1):
            row = []
            for x in range(-radius, radius + 1):
                # Using the circle equation (x²/a² + y²/b² ≤ 1)
                if x*x + y*y <= radius*radius:
                    row.append(symbol)
                else:
                    row.append(' ')
            rows.append(''.join(row))
        return '\n'.join(rows)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a right-angled triangle with the specified dimensions using the given symbol.
        
        Args:
            width: Width of the triangle
            height: Height of the triangle
            symbol: Character to use for drawing
            
        Returns:
            Multi-line string representing the triangle
        """
        self._validate_inputs((width, height), symbol)
        rows = []
        for i in range(height):
            # Calculate number of symbols for current row using linear interpolation
            symbols_count = math.ceil((i + 1) * width / height)
            rows.append(symbol * symbols_count)
        return '\n'.join(rows)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """Draws a symmetrical pyramid with the specified height using the given symbol.
        
        Args:
            height: Height of the pyramid
            symbol: Character to use for drawing
            
        Returns:
            Multi-line string representing the pyramid
        """
        self._validate_inputs(height, symbol)
        rows = []
        width = 2 * height - 1  # Maximum width of the pyramid
        
        for i in range(height):
            symbols = 2 * i + 1  # Number of symbols in current row
            padding = (width - symbols) // 2  # Padding needed for centering
            row = ' ' * padding + symbol * symbols + ' ' * padding
            rows.append(row)
        return '\n'.join(rows)


def main():
    """Main function demonstrating the usage of AsciiArt class."""
    try:
        art = AsciiArt()
        
        # Example usage of all shapes
        print("Square (5x5):")
        print(art.draw_square(5, '*'))
        print("\nRectangle (6x4):")
        print(art.draw_rectangle(6, 4, '#'))
        print("\nCircle (diameter 7):")
        print(art.draw_circle(7, '@'))
        print("\nTriangle (5x5):")
        print(art.draw_triangle(5, 5, '+'))
        print("\nPyramid (height 4):")
        print(art.draw_pyramid(4, '$'))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
