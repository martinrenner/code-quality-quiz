class AsciiArt:
    """
    A class for generating ASCII art shapes.
    
    This class provides methods to create various ASCII art shapes
    such as squares, rectangles, circles, triangles, and pyramids.
    """
    
    @staticmethod
    def validate_input(width=None, height=None, symbol=None, diameter=None):
        """
        Validates input parameters for the drawing functions.
        
        Args:
            width (int, optional): Width of the shape.
            height (int, optional): Height of the shape.
            symbol (str, optional): Symbol to use for drawing.
            diameter (int, optional): Diameter for circular shapes.
            
        Raises:
            ValueError: If any parameter doesn't meet requirements.
            TypeError: If parameters have incorrect type.
        """
        # Validate dimensions (width, height, diameter)
        for name, value in [('width', width), ('height', height), ('diameter', diameter)]:
            if value is not None:
                if not isinstance(value, int):
                    raise TypeError(f"{name} must be an integer")
                if value <= 0:
                    raise ValueError(f"{name} must be positive")
                # Practical limit to prevent excessive memory usage
                if value > 100:
                    raise ValueError(f"{name} must be less than or equal to 100")
        
        # Validate the symbol
        if symbol is not None:
            if not isinstance(symbol, str):
                raise TypeError("symbol must be a string")
            if len(symbol) != 1:
                raise ValueError("symbol must be a single character")

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.
        
        Args:
            width (int): The width and height of the square.
            symbol (str): The character to use for drawing the square.
            
        Returns:
            str: A string representing the ASCII art square.
            
        Example:
            >>> print(AsciiArt.draw_square(3, '*'))
            ***
            ***
            ***
        """
        cls.validate_input(width=width, symbol=symbol)
        row = symbol * width
        return '\n'.join([row for _ in range(width)])

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to use for drawing the rectangle.
            
        Returns:
            str: A string representing the ASCII art rectangle.
            
        Example:
            >>> print(AsciiArt.draw_rectangle(5, 3, '#'))
            #####
            #####
            #####
        """
        cls.validate_input(width=width, height=height, symbol=symbol)
        row = symbol * width
        return '\n'.join([row for _ in range(height)])

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the specified symbol.
        
        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to use for drawing the circle.
            
        Returns:
            str: A string representing the ASCII art circle.
            
        Example:
            >>> print(AsciiArt.draw_circle(5, 'o'))
              o
             ooo
            ooooo
             ooo
              o
        """
        cls.validate_input(diameter=diameter, symbol=symbol)
        
        # Empty result for invalid diameter
        if diameter <= 0:
            return ""
        
        # Single character for diameter 1
        if diameter == 1:
            return symbol
        
        result = []
        radius = diameter // 2
        
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                # Use the equation of a circle: x² + y² ≤ r²
                # +0.5 helps to make it look more circular in ASCII
                if x**2 + y**2 <= (radius + 0.5)**2:
                    line.append(symbol)
                else:
                    line.append(' ')
            result.append(''.join(line))
        
        return '\n'.join(result)

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.
        
        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character to use for drawing the triangle.
            
        Returns:
            str: A string representing the ASCII art right-angled triangle.
            
        Example:
            >>> print(AsciiArt.draw_triangle(4, 3, '^'))
            ^
            ^^
            ^^^
            ^^^^
        """
        cls.validate_input(width=width, height=height, symbol=symbol)
        
        # Calculate the increment per row
        if height <= 1:
            return symbol * width
        
        increment = width / height
        result = []
        
        for i in range(1, height + 1):
            # Calculate how many symbols to draw in this row
            symbols_count = round(i * increment)
            result.append(symbol * symbols_count)
        
        return '\n'.join(result)

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.
        
        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to use for drawing the pyramid.
            
        Returns:
            str: A string representing the ASCII art pyramid.
            
        Example:
            >>> print(AsciiArt.draw_pyramid(3, '$'))
              $
             $$$
            $$$$$
        """
        cls.validate_input(height=height, symbol=symbol)
        
        result = []
        width = 2 * height - 1
        
        for i in range(1, height + 1):
            # Calculate number of symbols for current row
            symbols = 2 * i - 1
            # Calculate padding required for centering
            padding = (width - symbols) // 2
            
            row = ' ' * padding + symbol * symbols
            result.append(row)
        
        return '\n'.join(result)


def main():
    """
    Main function to demonstrate the ASCII art functionality.
    """
    print("Welcome to ASCII Art Generator!")
    print("-------------------------------")
    
    # Dictionary mapping menu options to functions
    options = {
        '1': ('Square', AsciiArt.draw_square, ['width', 'symbol']),
        '2': ('Rectangle', AsciiArt.draw_rectangle, ['width', 'height', 'symbol']),
        '3': ('Circle', AsciiArt.draw_circle, ['diameter', 'symbol']),
        '4': ('Triangle', AsciiArt.draw_triangle, ['width', 'height', 'symbol']),
        '5': ('Pyramid', AsciiArt.draw_pyramid, ['height', 'symbol']),
    }
    
    while True:
        print("\nChoose a shape to draw:")
        for key, (name, _, _) in options.items():
            print(f"{key}. {name}")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-5): ")
        
        if choice == '0':
            print("Thank you for using ASCII Art Generator. Goodbye!")
            break
            
        if choice not in options:
            print("Invalid choice. Please try again.")
            continue
            
        name, func, params = options[choice]
        args = {}
        
        try:
            # Collect parameters for the selected function
            for param in params:
                if param == 'symbol':
                    symbol = input(f"Enter the symbol to use (default is '*'): ") or '*'
                    args['symbol'] = symbol
                else:
                    # For numerical parameters
                    while True:
                        try:
                            value = int(input(f"Enter the {param}: "))
                            args[param] = value
                            break
                        except ValueError:
                            print(f"Please enter a valid number for {param}.")
            
            # Call the function with collected parameters
            result = func(**args)
            
            print(f"\n{name} ASCII Art:")
            print(result)
            
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
