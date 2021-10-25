

def lander_input_init(canvas):

    lander_input_lmb_pressed = False
    lander_input_rmb_pressed = False

    lander_input_dx = 0
    lander_input_dy = 0

    lander_input_prev_valid = False

    #canvas.bind_all('<KeyPress-Left>', self.move_left)
    #canvas.bind_all('<KeyPress-Right>', self.move_right)

    canvas.addEventListener('mousedown', lander_input_mouse_down, False)
    canvas.addEventListener('mouseup', lander_input_mouse_up, False)
    canvas.addEventListener('mousemove', lander_input_mouse_move, False)
    canvas.addEventListener('mouseout', lander_input_mouse_out, False)

    def oncontextmenu():
        return False


def lander_input_mouse_down(e):
    if e.which == 1:
        lander_input_lmb_pressed = True
    if e.which == 3:
        lander_input_rmb_pressed = True

def lander_input_mouse_up(e):
    if e.which == 1:
        lander_input_lmb_pressed = False
    if e.which == 3:
        lander_input_rmb_pressed = False

def lander_input_mouse_out(e):

    lander_input_prev_valid = False


def lander_input_mouse_move(e):
    x = e.layerX
    y = e.layerY

    if (lander_input_prev_valid):
        lander_input_dx += x - lander_input_prev_x
        lander_input_dy += y - lander_input_prev_y

    lander_input_prev_x = x
    lander_input_prev_y = y
    lander_input_prev_valid = True
