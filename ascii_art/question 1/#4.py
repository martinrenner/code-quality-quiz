
class AsciiArt:
    """
    A class for creating 2D ASCII art shapes.
    """

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a square of specified width using the specified symbol.

        :param width: The width (and height) of the square.
        :param symbol: The character to be used for drawing.
        :return: A multi-line string representing the square.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")
        
        return '\n'.join([symbol * width for _ in range(width)])

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of specified width and height using the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The character to be used for drawing.
        :return: A multi-line string representing the rectangle.
        """
        if not isinstance(width, int) or width <= 0 or not isinstance(height, int) or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")
        
        return '\n'.join([symbol * width for _ in range(height)])

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle of specified diameter using the specified symbol.

        :param diameter: The diameter of the circle.
        :param symbol: The character to be used for drawing.
        :return: A multi-line string representing the circle.
        """
        if not isinstance(diameter, int) or diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")
        
        radius = diameter // 2
        result = []
        for y in range(diameter):
            line = ''
            for x in range(diameter):
                dx = x - radius
                dy = y - radius
                if dx*dx + dy*dy <= radius*radius:
                    line += symbol
                else:
                    line += ' '
            result.append(line)
        return '\n'.join(result)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle of specified width and height using the specified symbol.

        :param width: The width of the triangle's base.
        :param height: The height of the triangle.
        :param symbol: The character to be used for drawing.
        :return: A multi-line string representing the triangle.
        """
        if not isinstance(width, int) or width <= 0 or not isinstance(height, int) or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")
        
        result = []
        for i in range(height):
            result.append(symbol * min(width, i + 1))
        return '\n'.join(result)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid of specified height using the specified symbol.

        :param height: The height of the pyramid.
        :param symbol: The character to be used for drawing.
        :return: A multi-line string representing the pyramid.
        """
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")
        
        result = []
        for i in range(height):
            padding = ' ' * (height - i - 1)
            line = symbol * (2 * i + 1)
            result.append(padding + line)
        return '\n'.join(result)


# Example usage
if __name__ == "__main__":
    art = AsciiArt()

    print("Square:")
    print(art.draw_square(5, '*'))
    
    print("\nRectangle:")
    print(art.draw_rectangle(4, 3, '#'))
    
    print("\nCircle:")
    print(art.draw_circle(5, 'O'))
    
    print("\nTriangle:")
    print(art.draw_triangle(5, 5, 'T'))
    
    print("\nPyramid:")
    print(art.draw_pyramid(5, 'P'))
