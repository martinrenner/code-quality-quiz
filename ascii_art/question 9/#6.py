class AsciiArt:
    """
    A class for generating ASCII art shapes.
    """

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of the given width, filled with the specified symbol.

        Args:
            width (int): The width of the square.
            symbol (str): The character to fill the square with.

        Returns:
            str: A multi-line string representing the ASCII art square.

        Raises:
            ValueError: If width is not positive or symbol is not a single character.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the given width and height, filled with the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to fill the rectangle with.

        Returns:
            str: A multi-line string representing the ASCII art rectangle.

        Raises:
            ValueError: If width or height are not positive, or symbol is not a single character.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle of the given diameter using ASCII art.

        The circle is approximated by considering points on the circumference
        and filling in the area within. The algorithm uses the midpoint circle
        algorithm to determine which points to fill.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to use for drawing the circle.

        Returns:
            str: A multi-line string representing the ASCII art circle.

        Raises:
            ValueError: If diameter is not positive or symbol is invalid.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")


        radius = diameter // 2
        offset = 0 if diameter % 2 != 0 else 1  # Adjust for even/odd diameters
        grid = [[' ' for _ in range(diameter)] for _ in range(diameter)]

        def draw_quarter_circle(cx, cy, x, y):
            # Fill points in all 8 octants
            points = [
                (cx + x, cy + y), (cx - x, cy + y), (cx + x, cy - y), (cx - x, cy - y),
                (cx + y, cy + x), (cx - y, cy + x), (cx + y, cy - x), (cx - y, cy - x),
            ]
            for px, py in points:
                if 0 <= px < diameter and 0 <= py < diameter:
                    grid[py][px] = symbol

        x = 0
        y = radius
        d = 1 - radius  # Initial decision parameter

        draw_quarter_circle(radius - offset + 1, radius, x, y)  # Center circle, offset for even
        while y > x:
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x - y) + 5
                y -= 1
            x += 1
            draw_quarter_circle(radius - offset + 1, radius, x, y)

        return '\n'.join(''.join(row) for row in grid) + '\n'

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle.

        Args:
            width (int): The width of the base of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character to fill the triangle with.

        Returns:
            str: A multi-line string representing the ASCII art triangle.

        Raises:
            ValueError: If width or height are not positive or if symbol is invalid
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")
        
        triangle = ""
        for row in range(1, height + 1):
          if row <= height:
            line_width = int(row * (width / height))
            triangle += symbol * line_width + "\n"
        return triangle


    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to fill the pyramid with.

        Returns:
            str: A multi-line string representing the ASCII art pyramid.

        Raises:
          ValueError: If height is not positive or symbol is invalid
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

        pyramid = ""
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            symbols = symbol * (2 * i - 1)
            pyramid += spaces + symbols + spaces + "\n"
        return pyramid



def main():
    """
    Main function to demonstrate the AsciiArt class.
    """
    art = AsciiArt()

    while True:
        print("\nChoose a shape to draw (or 'exit' to quit):")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Pyramid")

        choice = input("Enter your choice (1-5): ")

        if choice.lower() == 'exit':
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        symbol = input("Enter the symbol to use: ")

        try:
            if choice == '1':
                width = int(input("Enter width: "))
                print(art.draw_square(width, symbol))
            elif choice == '2':
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                print(art.draw_rectangle(width, height, symbol))
            elif choice == '3':
                diameter = int(input("Enter diameter: "))
                print(art.draw_circle(diameter, symbol))
            elif choice == '4':
                width = int(input("Enter width of the base: "))
                height = int(input("Enter height: "))
                print(art.draw_triangle(width, height, symbol))
            elif choice == '5':
                height = int(input("Enter height: "))
                print(art.draw_pyramid(height, symbol))

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

