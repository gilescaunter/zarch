import j3d/matrix
import j3d/vector
import j3d/light
import jd3/model
import j3d/util
import j3d/sort
import j3d/lander_clip

import lander/camera
import lander/models
import lander/ground
import lander/input
import lander/hud
import lander/physics


from tkinter import *

main = null
main_ctx = null

map = null
map_ctx = null

lander_light = new j3d_light(j3d_vector_normalize([1.0, -1.0, 0.0, 0.0]))
lander_clip = new j3d_clip([[1, 0, 0, 0],
          [0, 0, 1, 0],
          [-1, 0, 0, 0],
          [0, 0, -1, 0]])
lander_sort = new j3d_sort(64, 200, 2)

lander_ground = lander_ground_make(lander_ground_size)

def time():
    return new Date().getTime();

def draw():
    main_ctx.fillStyle = "#000000"
    lander_sort.clear(main_ctx)

    lander_sort.begin()

    cam = lander_camera_matrix(lander_ship.p[0], lander_ship.p[1], lander_ship.p[2], -lander_ship.r[1])

    lander_light.eye = lander_camera_eye()

    lander_ground_draw(cam)
    lander_physics_draw(cam)

    lander_sort.draw(main_ctx)

    lander_hud_draw(main_ctx)


avgtime = 0
last = time()

def frame():
    for i in range(avgtime/25):
        lander_physics_tick()

    draw()

    now = time()

    avgtime = avgtime * 0.95 + (now - last) * 0.05

    last = now

    setTimeout('frame()', 0)



master = Tk()

canvas_width = 400
canvas_height = 300
main_canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
main_canvas.pack()

y = int(canvas_height / 2)
main_canvas.create_line(0, y, canvas_width, y, fill="#476042")
init()

