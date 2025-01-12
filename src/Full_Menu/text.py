class Text(object):
    """
    Container to hold a string and colour
    Args:
    text: String to hold the Title
    colour: String to control the colour
    """

    def __init__(self, 
                 text: str, 
                 colour: str='default'):
        self.text = text
        
        colours = {
            "red": "\033[31m",
            "orange": "\033[38;5;208m",
            "yellow": "\033[33m",
            "green": "\033[32m",
            "blue": "\033[34m",
            "pink": "\033[38;5;213m",
            "default": "\033[0m"
        }

        self.reset = colours["default"]

        self.colour = colours[colour]

    def __str__(self) -> str:
        return f"{self.colour}{self.text}{self.reset}"
    
    def __len__(self) -> str:
        return len(self.text)
    
    def get_text(self) -> str:
        """
        Returns the text string
        """
        return self.text