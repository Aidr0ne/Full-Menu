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
t1 = Text("Sup", "blue")

top_t.set_bottom(False)

F = function.Function(t, '')
F1 = function.Function(t1, '')

h = header.Header(t, top_t, 10, 10)

print(h.content, end='')

b = body.Body([F, F1], mid_t, 10, 10)

print(b.content, end='')

f = footer.Footer(t, bot_t, 10, 10)

print(f.content)