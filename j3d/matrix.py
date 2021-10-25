import math

def j3d_matrix_transpose(a, d):
    if d is None:
        return [[a[0][0], a[1][0], a[2][0], a[3][0]],
                [a[0][1], a[1][1], a[2][1], a[3][1]],
                [a[0][2], a[1][2], a[2][2], a[3][2]],
                [a[0][3], a[1][3], a[2][3], a[3][3]]]
    else:
        for i in range(4):
            for j in range(i):
                t1 = a[i][j]
                t2 = a[j][i]

                d[i][j] = t2
                d[j][i] = t1

        return d


def j3d_matrix_invert_simple(a, d):

    m1 = [[a[0][0], a[1][0], a[2][0], 0.0],
    [a[0][1], a[1][1], a[2][1], 0.0],
    [a[0][2], a[1][2], a[2][2], 0.0],
    [0.0, 0.0, 0.0, 1.0]]

    m2 = [[1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [-a[3][0], -a[3][1], -a[3][2], 1.0]]

    return j3d_matrix_multiply(m2, m1, d)


def j3d_matrix_rotate_x(a, d):

    s = math.sin(a)
    c = math.cos(a)

    if d is None:
        return [[1, 0, 0, 0],
                [0, c, s, 0],
                [0, -s, c, 0],
                [0, 0, 0, 1]]
    else:
        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = 1
        d0[1] = 0
        d0[2] = 0
        d0[3] = 0

        d1[0] = 0
        d1[1] = c
        d1[2] = s
        d1[3] = 0

        d2[0] = 0
        d2[1] = -s
        d2[2] = c
        d2[3] = 0

        d3[0] = 0
        d3[1] = 0
        d3[2] = 0
        d3[3] = 1

        return d


def j3d_matrix_rotate_y(a, d):

    s = math.sin(a)
    c = math.cos(a)

    if d is None:
        return [[c, 0, -s, 0],
                [0, 1, 0, 0],
                [s, 0, c, 0],
                [0, 0, 0, 1]]
    else:
        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = c
        d0[1] = 0
        d0[2] = -s
        d0[3] = 0

        d1[0] = 0
        d1[1] = 1
        d1[2] = 0
        d1[3] = 0

        d2[0] = s
        d2[1] = 0
        d2[2] = c
        d2[3] = 0

        d3[0] = 0
        d3[1] = 0
        d3[2] = 0
        d3[3] = 1

        return d


def j3d_matrix_rotate_z(a, d):

    s = math.sin(a)
    c = math.cos(a)

    if d is None:
        return [[c, s, 0, 0],
                [-s, c, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]
    else:
        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = c
        d0[1] = s
        d0[2] = 0
        d0[3] = 0

        d1[0] = -s
        d1[1] = c
        d1[2] = 0
        d1[3] = 0

        d2[0] = 0
        d2[1] = 0
        d2[2] = 1
        d2[3] = 0

        d3[0] = 0
        d3[1] = 0
        d3[2] = 0
        d3[3] = 1

        return d


def j3d_matrix_translate(x, y, z, d):

    if d is None:
        return [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [x, y, z, 1]]
    else:
        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = 1
        d0[1] = 0
        d0[2] = 0
        d0[3] = 0

        d1[0] = 0
        d1[1] = 1
        d1[2] = 0
        d1[3] = 0

        d2[0] = 0
        d2[1] = 0
        d2[2] = 1
        d2[3] = 0

        d3[0] = x
        d3[1] = y
        d3[2] = z
        d3[3] = 1

        return d


def j3d_matrix_scale(x, y, z, d):

    if d is None:
        return [[x, 0, 0, 0],
                [0, y, 0, 0],
                [0, 0, z, 0],
                [0, 0, 0, 1]]
    else:
        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = x
        d0[1] = 0
        d0[2] = 0
        d0[3] = 0

        d1[0] = 0
        d1[1] = y
        d1[2] = 0
        d1[3] = 0

        d2[0] = 0
        d2[1] = 0
        d2[2] = z
        d2[3] = 0

        d3[0] = 0
        d3[1] = 0
        d3[2] = 0
        d3[3] = 1

        return d



def j3d_matrix_project(w, h, n, f, d):
    l = f - n

    if d is None:
        return [[2 * n / w, 0, 0, 0],
                [0, 2 * n / h, 0, 0],
                [0, 0, f / l, 1],
                [0, 0, -f * n / l, 0]]
    else:
        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = 2 * n / w
        d0[1] = 0
        d0[2] = 0
        d0[3] = 0

        d1[0] = 0
        d1[1] = 2 * n / h
        d1[2] = 0
        d1[3] = 0

        d2[0] = 0
        d2[1] = 0
        d2[2] = f / l
        d2[3] = 1

        d3[0] = 0
        d3[1] = 0
        d3[2] = -f * n / l
        d3[3] = 0

        return d



def j3d_matrix_null(d):

    if d is None:
        return [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    else:
        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = 0
        d0[1] = 0
        d0[2] = 0
        d0[3] = 0

        d1[0] = 0
        d1[1] = 0
        d1[2] = 0
        d1[3] = 0

        d2[0] = 0
        d2[1] = 0
        d2[2] = 0
        d2[3] = 0

        d3[0] = 0
        d3[1] = 0
        d3[2] = 0
        d3[3] = 0

        return d




def j3d_matrix_identity(d):

    if d is None:
        return [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]
    else:

        d0 = d[0]
        d1 = d[1]
        d2 = d[2]
        d3 = d[3]

        d0[0] = 1
        d0[1] = 0
        d0[2] = 0
        d0[3] = 0

        d1[0] = 0
        d1[1] = 1
        d1[2] = 0
        d1[3] = 0

        d2[0] = 0
        d2[1] = 0
        d2[2] = 1
        d2[3] = 0

        d3[0] = 0
        d3[1] = 0
        d3[2] = 0
        d3[3] = 1

        return d




def j3d_matrix_multiply(a, b, d):
    length = a.j3d_length

    if length is None:
        length = a.length

    if d is None:
        d = j3d_util_make2darray(length, 4)

    b0 = b[0]
    b1 = b[1]
    b2 = b[2]
    b3 = b[3]

    b00 = b0[0]
    b01 = b0[1]
    b02 = b0[2]
    b03 = b0[3]
    b10 = b1[0]
    b11 = b1[1]
    b12 = b1[2]
    b13 = b1[3]
    b20 = b2[0]
    b21 = b2[1]
    b22 = b2[2]
    b23 = b2[3]
    b30 = b3[0]
    b31 = b3[1]
    b32 = b3[2]
    b33 = b3[3]

    for i in range (length):
        ai = a[i]
        di = d[i]

        ai0 = ai[0]
        ai1 = ai[1]
        ai2 = ai[2]
        ai3 = ai[3]

        di[0] = ai0 * b00 + ai1 * b10 + ai2 * b20 + ai3 * b30
        di[1] = ai0 * b01 + ai1 * b11 + ai2 * b21 + ai3 * b31
        di[2] = ai0 * b02 + ai1 * b12 + ai2 * b22 + ai3 * b32
        di[3] = ai0 * b03 + ai1 * b13 + ai2 * b23 + ai3 * b33

    d.j3d_length = length

    return d


def j3d_matrix_dehomogenize(a, d):

    length = a.j3d_length

    if length is None:
        length = a.length

    if d is None:
        d = j3d_util_make2darray(length, 4)

    for i in range(length):
        ai = a[i]
        di = d[i]

        ai3 = ai[3]

        di[0] = ai[0] / ai3
        di[1] = ai[1] / ai3
        di[2] = ai[2] / ai3
        di[3] = 1.0

    d.j3d_length = length

    return d
