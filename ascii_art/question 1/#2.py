from typing import List
import math

class AsciiArt:
    """
    A class for generating various ASCII art shapes.
    Implements drawing functionality for basic geometric shapes.
    """
    
    @staticmethod
    def _validate_input(dimension: int, symbol: str) -> None:
        """
        Validates input parameters for all drawing functions.
        
        Args:
            dimension: Integer representing size of the shape
            symbol: String character to draw the shape with
            
        Raises:
            ValueError: If inputs are invalid
        """
        if not isinstance(dimension, int) or dimension <= 0:
            raise ValueError("Dimensions must be positive integers")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square with the specified width and symbol.
        
        Args:
            width: Width and height of the square
            symbol: Character to draw the square with
            
        Returns:
            Multi-line string representing the square
        """
        self._validate_input(width, symbol)
        rows = [symbol * width for _ in range(width)]
        return '\n'.join(rows)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle with the specified dimensions and symbol.
        
        Args:
            width: Width of the rectangle
            height: Height of the rectangle
            symbol: Character to draw the rectangle with
            
        Returns:
            Multi-line string representing the rectangle
        """
        self._validate_input(width, symbol)
        self._validate_input(height, symbol)
        rows = [symbol * width for _ in range(height)]
        return '\n'.join(rows)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle with the specified diameter and symbol.
        
        Args:
            diameter: Diameter of the circle
            symbol: Character to draw the circle with
            
        Returns:
            Multi-line string representing the circle
        """
        self._validate_input(diameter, symbol)
        
        radius = diameter // 2
        rows: List[str] = []
        
        for y in range(-radius, radius + 1):
            row = ""
            for x in range(-radius, radius + 1):
                # Using circle equation (x²/a² + y²/b² ≤ 1)
                if x*x + y*y <= radius*radius:
                    row += symbol
                else:
                    row += " "
            rows.append(row)
            
        return '\n'.join(rows)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle with the specified dimensions and symbol.
        
        Args:
            width: Width of the triangle
            height: Height of the triangle
            symbol: Character to draw the triangle with
            
        Returns:
            Multi-line string representing the triangle
        """
        self._validate_input(width, symbol)
        self._validate_input(height, symbol)
        
        rows = []
        for i in range(height):
            # Calculate symbols in current row using proportion
            symbols_count = math.ceil((i + 1) * width / height)
            rows.append(symbol * symbols_count)
            
        return '\n'.join(rows)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid with the specified height and symbol.
        
        Args:
            height: Height of the pyramid
            symbol: Character to draw the pyramid with
            
        Returns:
            Multi-line string representing the pyramid
        """
        self._validate_input(height, symbol)
        
        rows = []
        for i in range(height):
            # Calculate padding and symbols for current row
            spaces = " " * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            rows.append(spaces + symbols)
            
        return '\n'.join(rows)


def main():
    """
    Main function to demonstrate the ASCII art generator.
    """
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("Square (4x4):")
        print(ascii_art.draw_square(4, "*"))
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, "#"))
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, "@"))
        print("\nTriangle (5x3):")
        print(ascii_art.draw_triangle(5, 3, "+"))
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, "$"))
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
