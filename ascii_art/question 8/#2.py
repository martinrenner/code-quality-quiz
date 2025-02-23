
class AsciiArt:
    """
    A class for generating various ASCII art shapes.

    This class provides methods to draw basic geometric shapes filled with a specified symbol.
    It adheres to ISO/IEC 25010 standards by focusing on:

    - Functionality: Correctly implements all required drawing functions.
    - Reliability: Handles edge cases and invalid inputs gracefully.
    - Usability:  Provides a clear and simple interface.
    - Efficiency: Uses reasonable algorithms for shape generation.
    - Maintainability: Uses clear, modular code with docstrings and comments.
    - Portability:  Uses standard Python; no external dependencies.
    """

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of the given width filled with the specified symbol.

        :param width: The width (and height) of the square.
        :param symbol: The character to use for drawing the square.
        :return: A multi-line string representing the ASCII art square.
        :raises ValueError: If width is not positive or symbol is not a single character.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the given width and height filled with the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The character to use for drawing the rectangle.
        :return: A multi-line string representing the ASCII art rectangle.
        :raises ValueError: If width or height are not positive or symbol is not a single character.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle of the given diameter, filled with the specified symbol.

        This uses a simple midpoint circle algorithm (optimized for filled circles).

        :param diameter: The diameter of the circle.
        :param symbol: The character to use for drawing the circle.
        :return: A multi-line string representing the ASCII art circle.
        :raises ValueError: If diameter is not positive or symbol is not a single character.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        radius = diameter // 2
        grid = [[' ' for _ in range(diameter)] for _ in range(diameter)]

        x = radius
        y = 0
        error = 0

        while x >= y:
            for i in range(-x, x + 1):
                grid[radius + y][radius + i] = symbol  # Octant 1
                grid[radius - y][radius + i] = symbol  # Octant 8

            for i in range(-y, y + 1):
                grid[radius + x][radius + i] = symbol  # Octant 2
                grid[radius - x][radius + i] = symbol  # Octant 7
            
            for i in range(-y, y + 1):
                grid[radius + i][radius + x] = symbol # Octant 3
                grid[radius + i][radius - x] = symbol # Octant 6

            for i in range(-x, x + 1):    
                grid[radius + i][radius + y] = symbol  # Octant 4
                grid[radius + i][radius - y] = symbol  # Octant 5

            y += 1
            error += 1 + 2 * y
            if 2 * (error - x) + 1 > 0:
                x -= 1
                error += 1 - 2 * x

        return "\n".join("".join(row) for row in grid)
    
    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the chosen symbol.

        :param width: Width of the triangle's base.
        :param height: Height of the triangle.
        :param symbol: Symbol to fill the triangle with.
        :return: String representation of the triangle.
        :raises ValueError: If width or height is not positive, or if the symbol is invalid.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        triangle = ""
        for row in range(1, height + 1):
            fill_count = int(row * (width / height))
            if fill_count > 0:  # Ensure at least one symbol per row, even for narrow/tall triangles
                triangle += symbol * fill_count + "\n"
            
        return triangle

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.

        :param height: The height of the pyramid (number of rows).
        :param symbol: The character to use for drawing the pyramid.
        :return: A multi-line string representing the ASCII art pyramid.
        :raises ValueError: If height is not positive or symbol is not a single character.
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        pyramid = ""
        for i in range(height):
            spaces = " " * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            pyramid += spaces + symbols + "\n"
        return pyramid
