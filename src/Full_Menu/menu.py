from Full_Menu.screen import Screen
from Full_Menu.Parts import body, footer, header

class Menu(object):
    """
    Container to hold the head, body and footer items.
        
    Args:
    head: The Header Used to create the Menu
    body: The Body used to create the Menu
    footer: The footer used to build the Menu
    screen: The Screen used to build the Menu
    """

    def __init__(self, 
                 head: header, 
                 body: body, 
                 footer: footer, 
                 screen: Screen=None):

        if screen == None:
            self.screen = Screen()
        else: self.screen = screen

        self.head = head
        self.body = body
        self.footer = footer


    def show(self) -> None:
        """
        Compiles the header, body and footer elements.

        Returns None
        """

        h = self.head.show()
        b = self.body.show()
        f = self.footer.show()

        c = h + b + f
        lines = c.splitlines()
        num = len(lines)

        empty_space = self.screen.get_height() - num

        self.footer.empty_space(empty_space)

        f = self.footer.show()

        print(empty_space)

        print(h, end='')
        print(b, end='')
        print(f)

        return None
