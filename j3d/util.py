import math

def j3d_util_make2darray(d1, d2):

    res = []

    for i in range(d1):
        res[i] = []

    return res

# I don't think this is needed
#def j3d_util_makeobjectarray(d):

    #res = []

    #for i in range(d):
     #   res[i] = new Object()

    #return res

def j3d_util_rgbcolor(r, g, b):
    r = math.floor(r)
    g = math.floor(g)
    b = math.floor(b)

    if (r > 255):
        r = 255;
    if (g > 255):
        g = 255;
    if (b > 255):
        b = 255;

    return "rgb(" + r + ", " + g + ", " + b + ")"



def j3d_util_rgbacolor(r, g, b, a):
    r = math.floor(r)
    g = math.floor(g)
    b = math.floor(b)

    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255

    if (a < 0.0):
        a = 0.0
    if (a > 1.0):
        a = 1.0

    return "rgba(" + r + ", " + g + ", " + b + ", " + a + ")"
