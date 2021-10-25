import math


def j3d_vector_copy(a):

    return [a[0], a[1], a[2], a[3]]


def j3d_vector_dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]


def j3d_vector_magnitude(a):
    a0 = a[0]
    a1 = a[1]
    a2 = a[2]
    a3 = a[3]

    return math.sqrt(a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3)


def j3d_vector_add(a, b, d):
    if d is None:
        return [a[0] + b[0],
                a[1] + b[1],
                a[2] + b[2],
                a[3] + b[3]]
    else:
        d[0] = a[0] + b[0]
        d[1] = a[1] + b[1]
        d[2] = a[2] + b[2]
        d[3] = a[3] + b[3]

        return d


def j3d_vector_subtract(a, b, d):

    if d is None:
        return [a[0] - b[0],
                a[1] - b[1],
                a[2] - b[2],
                a[3] - b[3]]
    else:
        d[0] = a[0] - b[0]
        d[1] = a[1] - b[1]
        d[2] = a[2] - b[2]
        d[3] = a[3] - b[3]

        return d


def j3d_vector_multiply(a, b, d):

    if d is None:
        return [a[0] * b,
                a[1] * b,
                a[2] * b,
                a[3] * b]
    else:
        d[0] = a[0] * b
        d[1] = a[1] * b
        d[2] = a[2] * b
        d[3] = a[3] * b

        return d


def j3d_vector_blend(a, b, f, d):

    e = 1 - f

    if d is None:
        return [e * a[0] + f * b[0],
                e * a[1] + f * b[1],
                e * a[2] + f * b[2],
                e * a[3] + f * b[3]]
    else:
        d[0] = e * a[0] + f * b[0]
        d[1] = e * a[1] + f * b[1]
        d[2] = e * a[2] + f * b[2]
        d[3] = e * a[3] + f * b[3]

    return d


def j3d_vector_cross(a, b, d):

    if d is None:
        return [a[1] * b[2] - a[2] * b[1],
                a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0],
                0.0]
    else:
        d[0] = a[1] * b[2] - a[2] * b[1]
        d[1] = a[2] * b[0] - a[0] * b[2]
        d[2] = a[0] * b[1] - a[1] * b[0]
        d[3] = 0.0

    return d


def j3d_vector_normalize(a, d):

    a0 = a[0]
    a1 = a[1]
    a2 = a[2]
    a3 = a[3]

    len1 = math.sqrt(a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3)

    if d is None:
        return [a0 / len1,
                a1 / len1,
                a2 / len1,
                a3 / len1]
    else:
        d[0] = a0 / len1
        d[1] = a1 / len1
        d[2] = a2 / len1
        d[3] = a3 / len1

        return d
