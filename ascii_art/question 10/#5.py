class AsciiArt:
    @staticmethod
    def validate_input(*args):
        """Validates input parameters for drawing functions.

        Args:
            *args: Variable length argument list for width, height, diameter, and symbol.

        Raises:
            ValueError: If any input is invalid.
        """
        for arg in args[:-1]:  # Exclude the last argument which is the symbol
            if not isinstance(arg, int) or arg <= 0:
                raise ValueError("Dimensions must be positive integers.")
        if not isinstance(args[-1], str) or len(args[-1]) != 1:
            raise ValueError("Symbol must be a single character string.")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """Draws a square of the specified width using the given symbol.

        Args:
            width (int): The width of the square.
            symbol (str): The character to use for filling the square.

        Returns:
            str: A string representing the square.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input(width, symbol)
        return '\n'.join([symbol * width for _ in range(width)])

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """Draws a rectangle of the specified width and height using the given symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to use for filling the rectangle.

        Returns:
            str: A string representing the rectangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input(width, height, symbol)
        return '\n'.join([symbol * width for _ in range(height)])

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """Draws an approximate circle of the specified diameter using the given symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to use for filling the circle.

        Returns:
            str: A string representing the circle.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input(diameter, symbol)
        radius = diameter // 2
        lines = []
        for y in range(diameter):
            line = ''
            for x in range(diameter):
                if (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2:
                    line += symbol
                else:
                    line += ' '
            lines.append(line)
        return '\n'.join(lines)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """Draws a right-angled triangle of the specified width and height using the given symbol.

        Args:
            width (int): The width of the triangle's base.
            height (int): The height of the triangle.
            symbol (str): The character to use for filling the triangle.

        Returns:
            str: A string representing the triangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input(width, height, symbol)
        lines = []
        for y in range(height):
            line = symbol * min(width, (y + 1) * width // height)
            lines.append(line)
        return '\n'.join(lines)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """Draws a symmetrical pyramid of the specified height using the given symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to use for filling the pyramid.

        Returns:
            str: A string representing the pyramid.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input(height, symbol)
        lines = []
        for y in range(height):
            spaces = ' ' * (height - y - 1)
            filled = symbol * (2 * y + 1)
            lines.append(spaces + filled)
        return '\n'.join(lines)
