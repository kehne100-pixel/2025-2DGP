from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
while (x < 780):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 5
    delay(0.01)

y = 90
while (y < 560) :
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(780, y)
    y = y + 5
    delay(0.01)

while (x > 10) :
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 560)
    x = x - 5
    delay(0.01)

while (y > 90) :
     clear_canvas_now()
     grass.draw_now(400, 30)
     character.draw_now(10, y)
     y = y - 5
     delay(0.01)


close_canvas()


