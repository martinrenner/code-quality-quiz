class AsciiArt:
    """
    A class for generating ASCII art shapes filled with specified characters.
    
    This class provides methods to create various ASCII art shapes such as squares,
    rectangles, circles, triangles, and pyramids with customizable dimensions and symbols.
    """
    
    @staticmethod
    def validate_input(dimension: int, symbol: str) -> None:
        """
        Validates the input parameters for ASCII art generation.
        
        Args:
            dimension (int): The dimension (width, height, etc.) of the shape.
            symbol (str): The character to be used for drawing the shape.
            
        Raises:
            ValueError: If dimensions are non-positive or symbol is not a single character.
        """
        if dimension <= 0:
            raise ValueError("Dimensions must be positive integers")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")
    
    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a square ASCII art.
        
        Args:
            width (int): The width and height of the square.
            symbol (str): The character to fill the square with.
            
        Returns:
            str: A multi-line string representing the square.
            
        Example:
            draw_square(3, '*') produces:
            ***
            ***
            ***
        """
        cls.validate_input(width, symbol)
        return cls.draw_rectangle(width, width, symbol)
    
    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangular ASCII art.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to fill the rectangle with.
            
        Returns:
            str: A multi-line string representing the rectangle.
            
        Example:
            draw_rectangle(4, 2, '#') produces:
            ####
            ####
        """
        cls.validate_input(width, symbol)
        cls.validate_input(height, symbol)
        
        row = symbol * width
        result = [row for _ in range(height)]
        return "\n".join(result)
    
    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle ASCII art.
        
        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character to fill the triangle with.
            
        Returns:
            str: A multi-line string representing the triangle.
            
        Example:
            draw_triangle(3, 3, '^') produces:
            ^
            ^^
            ^^^
        """
        cls.validate_input(width, symbol)
        cls.validate_input(height, symbol)
        
        result = []
        # Calculate how many symbols to add per row
        step = width / height
        
        for i in range(1, height + 1):
            # Calculate the number of symbols in this row
            num_symbols = round(i * step)
            result.append(symbol * num_symbols)
            
        return "\n".join(result)
    
    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid ASCII art.
        
        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to fill the pyramid with.
            
        Returns:
            str: A multi-line string representing the pyramid.
            
        Example:
            draw_pyramid(3, '@') produces:
              @
             @@@
            @@@@@
        """
        cls.validate_input(height, symbol)
        
        result = []
        width = 2 * height - 1  # Maximum width at the base of the pyramid
        
        for i in range(1, height + 1):
            # Calculate the number of symbols in this row
            num_symbols = 2 * i - 1
            # Calculate padding to center the symbols
            padding = (width - num_symbols) // 2
            
            line = " " * padding + symbol * num_symbols
            result.append(line)
            
        return "\n".join(result)
    
    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximation of a circle in ASCII art.
        
        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to fill the circle with.
            
        Returns:
            str: A multi-line string representing the circle.
            
        Example:
            draw_circle(5, 'o') produces:
             ooo
            ooooo
            ooooo
            ooooo
             ooo
        """
        cls.validate_input(diameter, symbol)
        
        result = []
        radius = diameter / 2
        
        for y in range(diameter):
            line = []
            for x in range(diameter):
                # Calculate the distance from center
                dx = x - radius + 0.5
                dy = y - radius + 0.5
                distance = (dx ** 2 + dy ** 2) ** 0.5
                
                # Add symbol if within the circle (with small buffer for better appearance)
                if distance <= radius + 0.1:
                    line.append(symbol)
                else:
                    line.append(" ")
                    
            result.append("".join(line))
            
        return "\n".join(result)


def main():
    """
    Main function to demonstrate the ASCII art generator functionality.
    """
    print("Welcome to the ASCII Art Generator!")
    print("Here are some examples of what this program can create:")
    
    print("\nSquare (4x4 with '#'):")
    print(AsciiArt.draw_square(4, "#"))
    
    print("\nRectangle (6x3 with '*'):")
    print(AsciiArt.draw_rectangle(6, 3, "*"))
    
    print("\nRight-angled Triangle (4x4 with '^'):")
    print(AsciiArt.draw_triangle(4, 4, "^"))
    
    print("\nPyramid (5 rows with '@'):")
    print(AsciiArt.draw_pyramid(5, "@"))
    
    print("\nCircle (diameter 9 with 'o'):")
    print(AsciiArt.draw_circle(9, "o"))
    
    print("\nTry creating your own ASCII art!")


if __name__ == "__main__":
    main()