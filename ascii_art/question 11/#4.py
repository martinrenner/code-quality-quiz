class AsciiArt:
    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.

        Args:
            width (int): The width of the square.
            symbol (str): The symbol to fill the square.

        Returns:
            str: A multi-line string representing the ASCII art of the square.

        Raises:
            ValueError: If width is less than 1 or symbol is not a single character.
        """
        if width < 1:
            raise ValueError("Width must be at least 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to fill the rectangle.

        Returns:
            str: A multi-line string representing the ASCII art of the rectangle.

        Raises:
            ValueError: If width or height is less than 1 or symbol is not a single character.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be at least 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the specified symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to fill the circle.

        Returns:
            str: A multi-line string representing the ASCII art of the circle.

        Raises:
            ValueError: If diameter is less than 1 or symbol is not a single character.
        """
        if diameter < 1:
            raise ValueError("Diameter must be at least 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        radius = diameter // 2
        result = []

        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                if x**2 + y**2 <= radius**2:
                    line.append(symbol)
                else:
                    line.append(' ')
            result.append(''.join(line))

        return '\n'.join(result)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.

        Args:
            width (int): The width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to fill the triangle.

        Returns:
            str: A multi-line string representing the ASCII art of the triangle.

        Raises:
            ValueError: If width or height is less than 1 or symbol is not a single character.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be at least 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        result = []
        for i in range(height):
            result.append(symbol * (i + 1))

        return '\n'.join(result)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to fill the pyramid.

        Returns:
            str: A multi-line string representing the ASCII art of the pyramid.

        Raises:
            ValueError: If height is less than 1 or symbol is not a single character.
        """
        if height < 1:
            raise ValueError("Height must be at least 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        result = []
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            line = symbol * (2 * i + 1)
            result.append(spaces + line + spaces)

        return '\n'.join(result)

# Example usage:
if __name__ == "__main__":
    art = AsciiArt()
    print(art.draw_square(5, '#'))
    print(art.draw_rectangle(5, 3, '#'))
    print(art.draw_circle(9, '#'))
    print(art.draw_triangle(5, 5, '#'))
    print(art.draw_pyramid(5, '#'))
