from tkinter import *
import time
import random
import time
import lander.physics as lp
import lander.input as li
import lander.ground as lg
import j3d.light as jl
import j3d.clip as jc
import j3d.sort as js
import j3d.vector as jv
import lander.camera as lc
import lander.hud as lh

tk = Tk()
tk.title('Zarch')
canvas_width = 400
canvas_height = 300
main_canvas = Canvas(tk, width=canvas_width, height=canvas_height)
main_canvas.pack()


tk_map = Tk()
tk_map.title('Map')
map_canvas = Canvas(tk,width=64,height = 64)
map_canvas.pack()

tk.update()
tk_map.update()

lander_light = jl.j3d_light(jv.j3d_vector_normalize([1.0, -1.0, 0.0, 0.0]))
lander_clip = jc.j3d_clip([[1, 0, 0, 0], [0, 0, 1, 0], [-1, 0, 0, 0], [0, 0, -1, 0]])
lander_sort = js.j3d_sort(64, 200, 2)

lander_ground = lg.lander_ground_make(lg.lander_ground_size)

avgtime = 0
last = time.time()

def draw(canvas):

    main_ctx.fillStyle = "#000000"
    lander_sort.clear(main_ctx)

    lander_sort.begin()
    cam = lc.lander_camera_matrix(lander_ship.p[0], lander_ship.p[1], lander_ship.p[2], -lander_ship.r[1])

    lander_light.eye = lc.lander_camera_eye()

    lg.lander_ground_draw(cam)
    lp.lander_physics_draw(cam)

    lander_sort.draw(main_canvas)

    lh.lander_hud_draw(main_canvas)




def frame():
    for i in range(avgtime/25):
        lp.lander_physics_tick()

    draw()

    now = time.time()

    avgtime = avgtime * 0.95 + (now - last) * 0.05

    last = now

    #setTimeout('frame()', 0)


def init():
    lp.lander_physics_init(main_canvas)
    li.lander_input_init(main_canvas)
    lg.lander_ground_init_map(map_canvas)

    frame()


init()

y = int(canvas_height / 2)
main_canvas.create_line(0, y, canvas_width, y, fill="#476042")

while 1:
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)

