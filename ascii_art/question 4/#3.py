
class AsciiArt:
    """
    A class for generating ASCII art shapes.
    """

    def _validate_input(self, size: int, symbol: str) -> None:
        """
        Validates the input size and symbol.

        :param size: The size parameter (width, height, etc.).
        :param symbol: The character to use for drawing.
        :raises ValueError: If size is not positive or symbol is not a single printable character.
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    def _validate_rectangle_input(self, width: int, height: int, symbol: str) -> None:
        """
        Validates the input width, height, and symbol for rectangle and triangle.

        :param width: the width of the shape
        :param height: the height of the shape
        :param symbol: The character to use for drawing.
        :raises ValueError: If size is not positive or symbol is not a single printable character.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of the given width filled with the specified symbol.

        :param width: The width of the square.
        :param symbol: The character to use for drawing.
        :return: A multi-line string representing the square.
        :raises ValueError: If input is invalid.
        """
        self._validate_input(width, symbol)
        return "\n".join([symbol * width for _ in range(width)])

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the given width and height, filled with the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The character to use for drawing.
        :return: A multi-line string representing the rectangle.
        :raises ValueError: If input is invalid.
        """
        self._validate_rectangle_input(width, height, symbol)
        return "\n".join([symbol * width for _ in range(height)])

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle of the given diameter, filled with the specified symbol.

        :param diameter: The diameter of the circle.
        :param symbol: The character to use for drawing.
        :return: A multi-line string representing the circle.
        :raises ValueError: If input is invalid.
        """
        self._validate_input(diameter, symbol)
        radius = diameter / 2
        result = []
        for y in range(-int(radius), int(radius) + 1):
            line = ""
            for x in range(-int(radius), int(radius) + 1):
                distance = (x * x + y * y) ** 0.5
                if distance <= radius:
                    line += symbol
                else:
                    line += " "  # Use space for outside the circle
            result.append(line)
        return "\n".join(result)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle.

        :param width: The width of the base of the triangle.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing.
        :return: String representation of the triangle.
        :raises ValueError: If input is invalid.
        """
        self._validate_rectangle_input(width, height, symbol)
        result = []
        for row in range(height):
            # Calculate the number of symbols to draw in this row
            num_symbols = int((row + 1) * (width / height))
            result.append(symbol * num_symbols)
        return "\n".join(result)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid with the given height.

        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing.
        :return: String representation of the pyramid.
        :raises ValueError: If input is invalid.
        """
        self._validate_input(height, symbol)
        result = []
        for row in range(height):
            spaces = " " * (height - row - 1)
            symbols = symbol * (2 * row + 1)
            result.append(spaces + symbols)
        return "\n".join(result)


# Test Cases
import unittest

class TestAsciiArt(unittest.TestCase):

    def setUp(self):
        self.art = AsciiArt()

    def test_draw_square(self):
        self.assertEqual(self.art.draw_square(3, "*"), "***\n***\n***")
        self.assertEqual(self.art.draw_square(1, "#"), "#")
        with self.assertRaises(ValueError):
            self.art.draw_square(-1, "*")
        with self.assertRaises(ValueError):
            self.art.draw_square(5, "ab")
        with self.assertRaises(ValueError):
            self.art.draw_square(5, "")

    def test_draw_rectangle(self):
        self.assertEqual(self.art.draw_rectangle(4, 2, "$"), "$$$$\n$$$$")
        self.assertEqual(self.art.draw_rectangle(2, 3, "%"), "%%\n%%\n%%")
        with self.assertRaises(ValueError):
            self.art.draw_rectangle(-1, 2, "*")
        with self.assertRaises(ValueError):
            self.art.draw_rectangle(5, 0, "*")

    def test_draw_circle(self):
        expected_circle_3 = " *** \n*****\n *** "
        self.assertEqual(self.art.draw_circle(3, "*"), expected_circle_3)
    
        expected_circle_5 = "  ***  \n ***** \n*******\n ***** \n  ***  "
        self.assertEqual(self.art.draw_circle(5, "*"), expected_circle_5)
         
        with self.assertRaises(ValueError):
            self.art.draw_circle(-1, "*")
        with self.assertRaises(ValueError):
            self.art.draw_circle(5, "ab")
        with self.assertRaises(ValueError):
            self.art.draw_circle(5, "")

    def test_draw_triangle(self):
        self.assertEqual(self.art.draw_triangle(3, 3, "*"), "*\n**\n***")
        self.assertEqual(self.art.draw_triangle(5,3, "#"), "#\n##\n###")
        with self.assertRaises(ValueError):
            self.art.draw_triangle(3, -3, "*")
        with self.assertRaises(ValueError):
            self.art.draw_triangle(-3, 3, "*")

    def test_draw_pyramid(self):
        self.assertEqual(self.art.draw_pyramid(3, "*"), "  *\n ***\n*****")
        self.assertEqual(self.art.draw_pyramid(1, "#"), "#")
        with self.assertRaises(ValueError):
            self.art.draw_pyramid(-1, "*")
        with self.assertRaises(ValueError):
            self.art.draw_pyramid(5, "ab")
        with self.assertRaises(ValueError):
            self.art.draw_pyramid(5, "")
            
if __name__ == '__main__':
    unittest.main()

