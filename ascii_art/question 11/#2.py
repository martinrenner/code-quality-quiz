class AsciiArt:
    """
    A class used to generate ASCII art shapes.

    Methods:
        draw_square(width: int, symbol: str) -> str: Draws a square.
        draw_rectangle(width: int, height: int, symbol: str) -> str: Draws a rectangle.
        draw_circle(diameter: int, symbol: str) -> str: Draws an approximate circle.
        draw_triangle(width: int, height: int, symbol: str) -> str: Draws a right-angled triangle.
        draw_pyramid(height: int, symbol: str) -> str: Draws a symmetrical pyramid.
    """

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a square filled with the given symbol.

        Args:
            width (int): The width of the square.
            symbol (str): The symbol to fill the square.

        Returns:
            str: A multi-line string representing the ASCII square.

        Raises:
            ValueError: If width is less than 1.
        """
        if width < 1:
            raise ValueError("Width must be at least 1.")
        return '\n'.join([symbol * width for _ in range(width)])

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the given symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to fill the rectangle.

        Returns:
            str: A multi-line string representing the ASCII rectangle.

        Raises:
            ValueError: If width or height is less than 1.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be at least 1.")
        return '\n'.join([symbol * width for _ in range(height)])

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the given symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to fill the circle.

        Returns:
            str: A multi-line string representing the ASCII circle.

        Raises:
            ValueError: If diameter is less than 1.
        """
        if diameter < 1:
            raise ValueError("Diameter must be at least 1.")

        radius = diameter // 2
        result = []
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                if x*x + y*y <= radius*radius:
                    line.append(symbol)
                else:
                    line.append(' ')
            result.append(''.join(line))
        return '\n'.join(result)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the given symbol.

        Args:
            width (int): The width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to fill the triangle.

        Returns:
            str: A multi-line string representing the ASCII triangle.

        Raises:
            ValueError: If width or height is less than 1.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be at least 1.")

        result = []
        for i in range(height):
            result.append(symbol * (i + 1))
        return '\n'.join(result)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the given symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to fill the pyramid.

        Returns:
            str: A multi-line string representing the ASCII pyramid.

        Raises:
            ValueError: If height is less than 1.
        """
        if height < 1:
            raise ValueError("Height must be at least 1.")

        result = []
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            fill = symbol * (2 * i + 1)
            result.append(spaces + fill + spaces)
        return '\n'.join(result)

# Example usage
if __name__ == "__main__":
    art = AsciiArt()
    print(art.draw_square(5, '#'))
    print(art.draw_rectangle(5, 3, '#'))
    print(art.draw_circle(10, '#'))
    print(art.draw_triangle(5, 5, '#'))
    print(art.draw_pyramid(5, '#'))
