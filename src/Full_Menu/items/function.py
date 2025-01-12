from Full_Menu.text import Text

class Function(object):
    """
    Item Used within a body element
    Runs a command when executed

    Args:
    text: The Text object used to show the item title
    command: The command to execute. 
    """
    def __init__(self, text: Text, command):
        self.command = command
        self.text = text

    def get_text(self) -> Text:
        """
        Returns The Stored text item
        """
        return self.text
    
    def get_command(self):
        """
        Returns the stored command
        """
        return self.command