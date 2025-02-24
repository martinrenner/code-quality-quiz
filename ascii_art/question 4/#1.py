import math

class AsciiArt:
    """
    A class for generating ASCII art shapes using a chosen printable symbol.
    Each static method returns a multi-line string representing the filled shape.
    """

    @staticmethod
    def validate_dimensions(*dimensions: int) -> None:
        """
        Validates that provided dimensions are positive integers.

        Args:
            *dimensions (int): Dimensions such as width, height or diameter.

        Raises:
            ValueError: If any dimension is not a positive integer.
        """
        for dim in dimensions:
            if not isinstance(dim, int) or dim <= 0:
                raise ValueError("Dimensions must be positive integers.")

    @staticmethod
    def validate_symbol(symbol: str) -> None:
        """
        Validates the symbol input.

        Args:
            symbol (str): The symbol used for drawing.

        Raises:
            ValueError: If the symbol is not a single character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a square of the given width using the specified symbol.

        Args:
            width (int): The side length of the square.
            symbol (str): The symbol to fill the square.

        Returns:
            str: A multi-line string representing the square.
        """
        AsciiArt.validate_dimensions(width)
        AsciiArt.validate_symbol(symbol)
        return "\n".join([symbol * width for _ in range(width)])

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the given width and height using the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to fill the rectangle.

        Returns:
            str: A multi-line string representing the rectangle.
        """
        AsciiArt.validate_dimensions(width, height)
        AsciiArt.validate_symbol(symbol)
        return "\n".join([symbol * width for _ in range(height)])

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle of the given diameter using the specified symbol.

        The circle is computed using the circle equation. Points that satisfy
        (x - center)^2 + (y - center)^2 <= radius^2 are filled.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to fill the circle.

        Returns:
            str: A multi-line string representing the circle.
        """
        AsciiArt.validate_dimensions(diameter)
        AsciiArt.validate_symbol(symbol)

        radius = diameter / 2
        center = (diameter - 1) / 2.0
        lines = []
        for y in range(diameter):
            line = ""
            for x in range(diameter):
                # Calculate the distance from the current point to the center.
                if (x - center) ** 2 + (y - center) ** 2 <= radius ** 2:
                    line += symbol
                else:
                    line += " "
            lines.append(line)
        return "\n".join(lines)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle with the given base width and height using the specified symbol.
        The right angle is positioned at the bottom left.

        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to fill the triangle.

        Returns:
            str: A multi-line string representing the triangle.
        """
        AsciiArt.validate_dimensions(width, height)
        AsciiArt.validate_symbol(symbol)

        lines = []
        # Generate each row with a number of symbols proportional to the row index.
        for i in range(1, height + 1):
            # Ensure that the bottom row is exactly the base width.
            row_width = round(i * width / height)
            row_width = max(1, row_width)
            lines.append(symbol * row_width)
        return "\n".join(lines)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid with the given height using the specified symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to fill the pyramid.

        Returns:
            str: A multi-line string representing the pyramid.
        """
        AsciiArt.validate_dimensions(height)
        AsciiArt.validate_symbol(symbol)

        lines = []
        base_width = 2 * height - 1
        for i in range(height):
            num_symbols = 2 * i + 1
            num_spaces = (base_width - num_symbols) // 2
            # Center the row by padding with spaces on both sides.
            lines.append(" " * num_spaces + symbol * num_symbols + " " * num_spaces)
        return "\n".join(lines)

def main():
    """
    Console-based 2D ASCII Art Application.
    
    This interactive application allows the user to choose a shape,
    input the required parameters (e.g., dimensions and drawing symbol),
    and then view the generated ASCII art.
    """
    print("Welcome to the ASCII Art Generator!")
    print("-----------------------------------")
    
    while True:
        print("\nSelect a shape to draw:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Right-angled Triangle")
        print("5. Pyramid")
        print("q. Quit")
        
        choice = input("Enter your choice: ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        
        try:
            if choice == '1':
                # Square
                width = int(input("Enter the side length of the square: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = AsciiArt.draw_square(width, symbol)
            elif choice == '2':
                # Rectangle
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = AsciiArt.draw_rectangle(width, height, symbol)
            elif choice == '3':
                # Circle
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = AsciiArt.draw_circle(diameter, symbol)
            elif choice == '4':
                # Right-angled Triangle
                width = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = AsciiArt.draw_triangle(width, height, symbol)
            elif choice == '5':
                # Pyramid
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = AsciiArt.draw_pyramid(height, symbol)
            else:
                print("Invalid choice. Please try again.")
                continue
            
            print("\nGenerated ASCII Art:\n")
            print(result)
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
