from screen import Screen
from text import Text
from Parts import footer, header, body
from theme import Theme
from items import function
from menu import Menu

top_t = Theme('│', '│', '─', '─', ('┌', '┐', '├', '┤'))
mid_t = Theme('│', '│', '─', '─', ('├', '┤', '├', '┤'))
bot_t = Theme('│', '│', '─', '─', ('├', '┤', '└', '┘'))

s = Screen()

t = Text("hello", "red")

top_t.set_bottom(False)

F = function.Function(t, '')

h = header.Header(t, top_t, s.get_width(), 10)

b = body.Body([F], mid_t, s.get_width(), 20)

f = footer.Footer(t, bot_t, s.get_width(), 10)

m = Menu(h, b, f, s)

m.show()