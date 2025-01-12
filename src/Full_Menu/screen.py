import os
import subprocess
import platform

class Screen(object):
    """
    Creates a Screen Used as a abstraction layer when interacting with the terminal
    """

    def __init__(self):
        self.resize()

    def fill(self, character: str) -> None:
        """
        Test function to fill the screen

        Args:
        character: Character to fill Screen with eg(h)
        """
        for y in range(self.height):
            for x in range(self.width):
                print(character, end='')
            print(' ')

        return None

    def clear(self) -> None:
        """
        Clears The screen
        """
        if platform.system() == "Windows":
            subprocess.check_call('cls', shell=True)
        else:
            print(subprocess.check_output('clear').decode())

        return None

    def resize(self) -> None:
        """
        Sets size to the terminal size
        """
        size = os.get_terminal_size()
        self.width =  size.columns
        self.length = size.lines

        return None

    def get_width(self) -> int:
        """
        Returns Width
        """
        return self.width

    def get_height(self) -> int:
        """
        Returns Length
        """
        return self.length


