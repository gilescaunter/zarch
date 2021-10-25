import math
import lander.ground as lg
import constants as c
import j3d.vector as jv
import j3d.matrix as jm

lander_physics_g = [0, 0.003, 0, 0]
lander_physics_a = [0, -0.01, 0, 0]

def lander_physics_adjust(v):
    if (v[0] < lander_ship.p[0] - lander_ground_size / 2):
        v[0] += lander_ground_size
    elif (v[0] > lander_ship.p[0] + lander_ground_size / 2):
        v[0] -= lander_ground_size

    if (v[2] < lander_ship.p[2] - lander_ground_size / 2):
        v[2] += lander_ground_size
    elif (v[2] > lander_ship.p[2] + lander_ground_size / 2):
        v[2] -= lander_ground_size

class Dot:

    def __init__(self, _p, _v):
        t = 0
        p = _p
        v = _v

    def tick():
        self.t += 1

        v = jv.j3d_vector_add(v, lander_physics_g)
        p = jv.j3d_vector_add(p, v)

        lander_physics_adjust(p)

        return t > 16 or p[1] >= lg.lander_ground_height(p[0], p[2])


    def draw(cam):
        vec1 = j3d_matrix_multiply([p], cam)
        vec2 = j3d_matrix_dehomogenize(vec1)

        lander_sort.add_particle(vec2[0], j3d_util_rgbacolor(255, 255, 255, (17 - t) / 16), 1, 0, -0.04)


class Bullet():
    def __init__(self,_p, _v, _kind):

        p = _p
        v = _v

        kind = _kind;

        def tick():
            v = jv.j3d_vector_add(v, lander_physics_g)
            p = jv.j3d_vector_add(p, v)

            lander_physics_adjust(p)

            if (kind == c.lander_bullet_kind_player):
                for i in range(lander_aliens.length):
                    if (lander_aliens[i].check_bullet(p)):
                        return True

            else:
                if (lander_ship.check_bullet(p)):
                    return True

            return p[1] >= lg.lander_ground_height(p[0], p[2]);

        def draw(cam):
            if (p[0] > lander_ship.p[0] - c.lander_ground_range
                    and p[0] < lander_ship.p[0] + c.lander_ground_range
                    and p[2] > lander_ship.p[2] - c.lander_ground_range
                    and p[2] < lander_ship.p[2] + c.lander_ground_range):
                vec1 = jm.j3d_matrix_multiply([p], cam)
                vec2 = jm.j3d_matrix_dehomogenize(vec1)

                lander_sort.add_particle(vec2[0], ju.j3d_util_rgbcolor(255, 255, 255), 2, 0, -0.04)

class debris():
    def __init__(self,_p,_v):
        p = _p
        v = _v
        r = [math.random() * math.PI * 2, math.random() * math.PI * 2, math.random() * math.PI * 2, 0];
        w = [math.random() * 0.2 - 0.1, math.random() * 0.2 - 0.1, math.random() * 0.2 - 0.1, 0];


    def matrix(p, r):
        mat_rx = jm.j3d_matrix_rotate_x(r[0])
        mat_ry = jm.j3d_matrix_rotate_y(r[1])
        mat_rz = jm.j3d_matrix_rotate_z(r[2])
        mat_tr = jm.j3d_matrix_translate(p[0], p[1], p[2])

        mat1 = jm.j3d_matrix_multiply(mat_rx, mat_ry)
        mat2 = jm.j3d_matrix_multiply(mat1, mat_rz)
        mat3 = jm.j3d_matrix_multiply(mat2, mat_tr)

        return mat3

    def tick():
        v = j3d_vector_add(v, lander_physics_g)
        p = j3d_vector_add(p, v)
        r = j3d_vector_add(r, w)

        lander_physics_adjust(p)

        return v[1] > 0 and p[1] >= c.lander_ground_height(p[0], p[2])

    def draw(cam):
        mat = matrix(p, r)

        model1 = lander_clip.clip_model(lander_model_debris, mat, model1)
        lander_light.light_model(model1, mat)
        model2 = jm.j3d_model_multiply(model1, jm.j3d_matrix_multiply(mat, cam), model2)
        model3 = jm.j3d_model_dehomogenize(model2, model3)

        lander_sort.add_model(model3, 0)




class Alien():
    def __init__(self, _p, a):
        speed = 0.02

        bullet_speed = 0.05

        width = alien1_a
        height = alien1_c

        state_flying = lander_alien_state_flying
        state_dead = lander_alien_state_dead

        t = 100
        c = 0

        p = _p
        v = [speed * math.sin(a), 0, speed * math.cos(a), 0]
        r = 0.0

        health = 1.0

        state = state_flying

        this.p = p

        this.alpha = 0.0

    def get_state():
        return self.state


    def matrix(p, r):

        mat_ry = jm.j3d_matrix_rotate_y(r)
        mat_tr = jm.j3d_matrix_translate(p[0], p[1], p[2])

        mat1 = jm.j3d_matrix_multiply(mat_ry, mat_tr)

        return mat1

    def tick():
        if (state == state_flying):

            p = jv.j3d_vector_add(p, v, p)
            r += 0.04

            p[1] = c.lander_ground_height(p[0], p[2]) - 3

            lander_physics_adjust(p)

            s = jv.j3d_vector_subtract(lander_ship.p, p)
            h = s[1]

            s[1] = 0.0

            r = j3d_vector_magnitude(s)

            if (r > 1 and r < 5 and h > -5 and t < 0):
                bullet_p = p
                bullet_v = jv.j3d_vector_multiply(jv.j3d_vector_normalize(s), c.bullet_speed)

                r /= c.bullet_speed

                bullet_v[1] = h / r - 0.5 * lander_physics_g[1] * r

                lander_physics_objects.append(Bullet(bullet_p, bullet_v, c.lander_bullet_kind_enemy))

                c+=1
                if (c < 5):
                    t = 6
                else:
                    t = 120
                    c = 0


            else:
                t-=1

        return False


    def check_bullet(bullet_p):
        if (state == state_flying
                and bullet_p[0] > p[0] - c.width
                and bullet_p[0] < p[0] + c.width
                and bullet_p[1] > p[1] - c.height
                and bullet_p[1] < p[1] + c.height
                and bullet_p[2] > p[2] - c.width
                and bullet_p[2] < p[2] + c.width):
            health -= 0.2

            if (health <= 0.0):
                lander_physics_add_explosion(p)

                state = c.state_dead

                health = 1.0
                alpha = 0.0

                jv.j3d_vector_add(p, [16, 0, 16, 0], p)

            return True

        else:
            return False

    def draw(cam):
        if (state != c.state_dead):
            range = c.lander_ground_range + alien1_a

            if (p[0] > lander_ship.p[0] - range
                    and p[0] < lander_ship.p[0] + range
                    and p[2] > lander_ship.p[2] - range
                    and p[2] < lander_ship.p[2] + range):
                mat = matrix(p, r)

                model1 = lander_clip.clip_model(lander_model_alien1, mat, model1)
                lander_light.light_model(model1, mat)
                model2 = jm.j3d_model_multiply(model1, jm.j3d_matrix_multiply(mat, cam), model2)
                model3 = jm.j3d_model_dehomogenize(model2, model3)

                lander_sort.add_model(model3, 0)



class Ship:

    def __init__(self, canvas, _p, _v):
        width = 0.5
        height = 0.2



        t = 0

        p = _p
        v = [0, 0, 0, 0]
        r = [0, Math.PI / 4, 0, 0]

        fuel = 0.0
        health = 1.0

        state = state_landed

        this.p = p
        this.r = r

        lander_input_lmb_pressed = False
        lander_input_rmb_pressed = False

        lander_input_dx = 0
        lander_input_dy = 0

        lander_input_prev_valid = False

        # canvas.bind_all('<KeyPress-Left>', self.move_left)
        # canvas.bind_all('<KeyPress-Right>', self.move_right)

        canvas.addEventListener('mousedown', self.lander_input_mouse_down, False)
        canvas.addEventListener('mouseup', self.lander_input_mouse_up, False)
        canvas.addEventListener('mousemove', self.lander_input_mouse_move, False)
        canvas.addEventListener('mouseout', self.lander_input_mouse_out, False)

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

    def get_fuel(self):
        return self.fuel

    def get_health():
        return self.health


    def matrix(p, r):
        mat_rx = jm.j3d_matrix_rotate_x(r[0])
        mat_ry = jm.j3d_matrix_rotate_y(r[1])
        mat_tr = jm.j3d_matrix_translate(p[0], p[1], p[2])

        mat1 = jm.j3d_matrix_multiply(mat_rx, mat_ry)
        mat2 = jm.j3d_matrix_multiply(mat1, mat_tr)

        return mat2

    def tick():
        if state == state_landed:
            fuel += 0.002
            if fuel > 1.0:
                fuel = 1.0
            if (self.lander_input_lmb_pressed):
                state = state_flying;


        if state == state_flying:
            r[0] += lander_input_dy / 32
            r[1] += lander_input_dx / 32

            if (r[0] < -math.PI / 2):
                r[0] = -math.PI / 2
            if (r[0] > math.PI / 2):
                r[0] = math.PI / 2

            mat = matrix(p, r)

            if (self.lander_input_lmb_pressed and fuel > 0.0):
                a = jm.j3d_matrix_multiply([lander_physics_a], mat)[0]

                j3d_vector_add(v, a, v)

                dot_p = j3d_matrix_multiply([[0.2 * math.random() - 0.1, 0.2, 0.2 * math.random() - 0.1, 1]], mat)[0]
                dot_v = j3d_matrix_multiply([[0.01 * math.random() - 0.005, 0.15 + 0.05 * math.random(), 0.01 * math.random() - 0.005, 0]], mat)[0]

                lander_physics_objects.append(Dot(dot_p, dot_v))

                fuel -= 0.0002

                if (fuel < 0.0):
                    fuel = 0.0


            if (self.lander_input_rmb_pressed and t < 0):
                bullet_p = jm.j3d_matrix_multiply([[0.0, 0.0, 0.3, 1.0]], mat)[0]
                bullet_v = jm.j3d_matrix_multiply([[0.0, 0.0, 0.2, 0.0]], mat)[0]

                lander_physics_objects.append(Bullet(bullet_p, bullet_v, c.lander_bullet_kind_player))

                t = 2
            else:
                t -= 1

            jv.j3d_vector_add(v, lander_physics_g, v)
            jv.j3d_vector_multiply(v, 0.98, v)

            jv.j3d_vector_add(p, v, p)

            height = c.lander_ground_height(p[0], p[2])

            if (p[1] > height):
                x = math.floor(p[0]) & c.lander_ground_mask
                z = math.floor(p[2]) & c.lander_ground_mask

                if (x >= c.lander_ground_pad_x
                        and x < c.lander_ground_pad_x + 4
                        and z >= c.lander_ground_pad_z
                        and z < c.lander_ground_pad_z + 4
                        and r[0] > -0.3 and r[0] < 0.3
                        and v[0] > -0.3 and v[0] < 0.3 and
                        v[1] > -0.1 and v[1] < 0.1 and
                        v[2] > -0.3 and v[2] < 0.3):
                    state = c.state_landed

                    p[1] = height
                    v =[0, 0, 0, 0]
                    r[0] = 0
                else:
                    state = state_dead

                    health = 0.0

                    lander_physics_add_explosion(p)



            lander_input_dx = 0
            lander_input_dy = 0

            return False


        def check_bullet(bullet_p):
            if (state != c.state_dead and
                    bullet_p[0] > p[0] - c.width and
                    bullet_p[0] < p[0] + c.width and
                    bullet_p[1] > p[1] - c.height and
                    bullet_p[1] < p[1] + c.height and
                    bullet_p[2] > p[2] - c.width and
                    bullet_p[2] < p[2] + c.width):
                health -= 0.02

                if (health <= 0.0):
                    lander_physics_add_explosion(p)
                    state = c.state_dead

                return True

            else:
                return False


    def draw(cam):
        if (state != state_dead):
            mat = matrix(p, r)

            lander_light.light_model(lander_model_ship, mat)
            model1 = j3d_model_multiply(lander_model_ship, j3d_matrix_multiply(mat, cam), model1)
            model2 = j3d_model_dehomogenize(model1, model2)
            lander_sort.add_model(model2, 1)



def lander_physics_add_explosion(p):
    for i in range(8):
        debris = lander_physics_debris(j3d_vector_copy(p), [0.1 * math.random() - 0.05, -0.05 * math.random() - 0.1, 0.1 * math.random() - 0.05, 0.0]);

        lander_physics_objects.push(debris)


lander_physics_objects = []
lander_aliens = []


def lander_physics_init(canvas):
    ship = Ship(canvas,[c.lander_ground_pad_x + 2, lg.lander_ground_height(c.lander_ground_pad_x + 2, c.lander_ground_pad_z + 2),c.lander_ground_pad_z + 2, 1])
    lander_physics_objects.append(ship)

    for i in range(4):
        alien = Alien([math.random() * c.lander_ground_size, 0, math.random() * c.lander_ground_size, 1], math.random() * math.PI * 2)

        lander_aliens.append(alien)
        lander_physics_objects.append(alien)

def lander_physics_tick():
    for i in range(lander_physics_objects.length):
        obj = lander_physics_objects[i]

        if (obj.tick()):
            lander_physics_objects.splice(i, 1)
        else:
            i += 1


def lander_physics_draw(cam):
    for i in range(lander_physics_objects.length):
        obj = lander_physics_objects[i]
        obj.draw(cam)
