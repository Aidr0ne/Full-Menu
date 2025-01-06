from screen import Screen
from text import Text
from Parts import footer, header, body
from theme import Theme
from items import function

top_t = Theme('│', '│', '─', '─', ('┌', '┐', '├', '┤'))
mid_t = Theme('│', '│', '─', '─', ('├', '┤', '├', '┤'))
bot_t = Theme('│', '│', '─', '─', ('├', '┤', '└', '┘'))

s = Screen()

t = Text("hello", "red")

top_t.set_bottom(False)

F = function.Function(t, '')

h = header.Header(t, top_t, 10, 10)

print(h.content, end='')

b = body.Body([F], mid_t, 10, 10)

print(b.content, end='')

f = footer.Footer(t, bot_t, 10, 10)

print(f.content)