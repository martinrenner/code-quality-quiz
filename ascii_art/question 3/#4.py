
class AsciiArt:
    def __init__(self):
        """
        Initialize the AsciiArt class. This class does not require parameters
        for initialization as it handles drawing shapes on demand.
        """
        pass

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.

        Args:
            width (int): The width (and height) of the square.
            symbol (str): A single character used to draw the square.

        Returns:
            str: A multi-line string representing the drawn square.

        Raises:
            ValueError: If width is less than 1 or if symbol is not a single character.
        """
        if width < 1:
            raise ValueError("Width must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([symbol * width for _ in range(width)])

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): A single character used to draw the rectangle.

        Returns:
            str: A multi-line string representing the drawn rectangle.

        Raises:
            ValueError: If width or height is less than 1 or if symbol is not a single character.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([symbol * width for _ in range(height)])

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the specified symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): A single character used to draw the circle.

        Returns:
            str: A multi-line string representing the drawn circle.

        Raises:
            ValueError: If diameter is less than 1 or if symbol is not a single character.
        """
        if diameter < 1:
            raise ValueError("Diameter must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        radius = diameter // 2
        return '\n'.join([
            ' ' * max(radius - int((radius ** 2 - (radius - y) ** 2) ** 0.5), 0) +
            symbol * (diameter - 2 * max(radius - int((radius ** 2 - (radius - y) ** 2) ** 0.5), 0))
            for y in range(diameter)
        ])

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.

        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): A single character used to draw the triangle.

        Returns:
            str: A multi-line string representing the drawn triangle.

        Raises:
            ValueError: If width or height is less than 1, or if symbol is not a single character.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([symbol * min((i + 1) * width // height, width) for i in range(height)])

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): A single character used to draw the pyramid.

        Returns:
            str: A multi-line string representing the drawn pyramid.

        Raises:
            ValueError: If height is less than 1 or if symbol is not a single character.
        """
        if height < 1:
            raise ValueError("Height must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([
            ' ' * (height - i - 1) + symbol * (2 * i + 1) for i in range(height)
        ])

# Example usage
if __name__ == "__main__":
    art = AsciiArt()
    print(art.draw_square(5, '#'))
    print(art.draw_rectangle(4, 3, '*'))
    print(art.draw_circle(5, 'O'))
    print(art.draw_triangle(5, 3, '+'))
    print(art.draw_pyramid(3, '@'))
