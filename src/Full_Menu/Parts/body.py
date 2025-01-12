from Full_Menu.theme import Theme
from Full_Menu.items.function import Function

class Body(object):
    """
    Container to hold The objects and theme

    Args:
    objects: list of objects
    theme: Theme object
    width: Amount of columns
    height: Amount of rows
    """
    def __init__(self, 
                 objects: list[Function], 
                 theme: Theme,
                 width: int, 
                 height: int):
        self.objects = objects
        self.theme = theme

        self.content = self.preload(width, height)


    def preload(self, width, height) -> str:
        if height < (5 + len(self.objects)):
            raise ValueError("Height is not big enough")
        
        self.theme.set_bottom(False)
        content = ''
        content += self.theme.render_top(width)
        content += self.theme.render_middle(True, width)
        for item in self.objects:
            tx = item.get_text()
            content += self.theme.render_middle(False, width, tx)
        content += self.theme.render_middle(True, width)
        content += self.theme.render_bottom(width)

        return content

    def show(self):
        return self.content