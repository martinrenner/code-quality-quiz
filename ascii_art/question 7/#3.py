"""
Console-based 2D ASCII ART Application

This application allows the user to draw various filled ASCII art shapes on the console.
Shapes available include:
  • Square
  • Rectangle
  • Approximate Circle
  • Right-angled Triangle
  • Pyramid

Each shape drawing function is implemented as a method of the AsciiArt class.
All methods validate inputs against malicious or invalid values ensuring that
dimensions are positive integers and that the symbol is a non‐empty string.

The code is structured for clarity, testability, and modularity, meeting the ISO/IEC 25010 requirements.
"""

class AsciiArt:
    """
    A class to generate 2D ASCII art shapes.
    """
    
    @staticmethod
    def _validate_dimension(name: str, value: int) -> None:
        """
        Validates that a dimension (width, height, diameter, etc.) is a positive integer.
        
        Args:
            name (str): The name of the dimension for error messages.
            value (int): The value to validate.
        
        Raises:
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Invalid value for {name}. It must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validates that the symbol is a non-empty string.
        
        Args:
            symbol (str): The symbol to use for drawing.
        
        Raises:
            ValueError: If the symbol is not a non-empty string.
        """
        if not isinstance(symbol, str) or not symbol:
            raise ValueError("Symbol must be a non-empty string.")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of the given width using the provided symbol.
        
        Args:
            width (int): The width (and height) of the square.
            symbol (str): The printable symbol used for drawing.
        
        Returns:
            str: A multi-line string that represents the square.
        """
        self._validate_dimension("width", width)
        self._validate_symbol(symbol)
        
        lines = []
        for _ in range(width):
            lines.append(symbol * width)
        return "\n".join(lines)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle with the provided width and height using the symbol.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The printable symbol used for drawing.
        
        Returns:
            str: A multi-line string that represents the rectangle.
        """
        self._validate_dimension("width", width)
        self._validate_dimension("height", height)
        self._validate_symbol(symbol)
        
        lines = []
        for _ in range(height):
            lines.append(symbol * width)
        return "\n".join(lines)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle of the given diameter using the provided symbol.
        
        The circle is approximated on a square grid. For each coordinate (x, y),
        if the distance from the center is less than or equal to the radius,
        the symbol is printed; otherwise, a space is printed.
        
        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The printable symbol used for drawing.
        
        Returns:
            str: A multi-line string that represents the circle.
        """
        self._validate_dimension("diameter", diameter)
        self._validate_symbol(symbol)
        
        center = (diameter - 1) / 2.0
        radius = diameter / 2.0
        lines = []
        for y in range(diameter):
            line_chars = []
            for x in range(diameter):
                if (x - center) ** 2 + (y - center) ** 2 <= radius ** 2:
                    line_chars.append(symbol)
                else:
                    line_chars.append(" ")
            lines.append("".join(line_chars))
        return "\n".join(lines)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle of the specified width and height using the provided symbol.
        
        The triangle is built row by row; each row contains a proportional number
        of symbols relative to the overall dimensions.
        
        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The printable symbol used for drawing.
        
        Returns:
            str: A multi-line string that represents the triangle.
        """
        self._validate_dimension("width", width)
        self._validate_dimension("height", height)
        self._validate_symbol(symbol)
        
        lines = []
        for i in range(height):
            # Ensure at least one symbol per row; force the last row to have exactly 'width' symbols.
            if i == height - 1:
                count = width
            else:
                count = max(1, round((i + 1) * width / height))
            lines.append(symbol * count)
        return "\n".join(lines)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid of the given height using the provided symbol.
        
        The pyramid is centered; each row has an odd number of symbols
        with appropriate spacing to maintain symmetry.
        
        Args:
            height (int): The height of the pyramid.
            symbol (str): The printable symbol used for drawing.
        
        Returns:
            str: A multi-line string that represents the pyramid.
        """
        self._validate_dimension("height", height)
        self._validate_symbol(symbol)
        
        total_width = 2 * height - 1  # base width of the pyramid
        lines = []
        for i in range(height):
            symbol_count = 2 * i + 1
            # Center the row within the total width
            line = (symbol * symbol_count).center(total_width)
            lines.append(line)
        return "\n".join(lines)


def main():
    """
    Main console loop for interactive shape drawing.
    The user is prompted to choose a shape and provide required inputs.
    """
    art = AsciiArt()
    print("Welcome to the ASCII Art App!")
    
    while True:
        print("\nChoose a shape to draw:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Right-angled Triangle")
        print("5. Pyramid")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "6":
            print("Thank you for using the ASCII Art App. Goodbye!")
            break
        elif choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please enter a number from 1 to 6.")
            continue

        # Try to get the required inputs and draw the selected shape.
        try:
            if choice == "1":
                width = int(input("Enter the width of the square: "))
                symbol = input("Enter the symbol: ")
                result = art.draw_square(width, symbol)
            elif choice == "2":
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter the symbol: ")
                result = art.draw_rectangle(width, height, symbol)
            elif choice == "3":
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter the symbol: ")
                result = art.draw_circle(diameter, symbol)
            elif choice == "4":
                width = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter the symbol: ")
                result = art.draw_triangle(width, height, symbol)
            elif choice == "5":
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter the symbol: ")
                result = art.draw_pyramid(height, symbol)
            
            print("\nHere is your ASCII art:\n")
            print(result)
        except ValueError as ve:
            print(f"Error: {ve}")


if __name__ == "__main__":
    main()
