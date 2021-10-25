import numpy as np
import random
import math
from tkinter import *

class RGB:


    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def add(self, r,g,b):
        return RGB (r + self.r, g + self.g, b + self.b);


    def subtract (self, r,g,b):
        return RGB (r - self.r, g - self.g, b - self.b);

    def scale (self, scale):
        return RGB (self.r * scale, self.g * scale, self.b * scale);

    def toInt (value):
        if value < 0.0:
            res = 0
        elif value > 1.0:
            res = 255
        else:
            res =  int(value * 255)
        return res

    def toRGB(self):
        return (0xff << 24) | self.toInt (self.r) << 16 | self.toInt (self.g) << 8 | self.toInt (self.b)

class Triple:

    def __init__(self,  x,  y,  z):
        self.x = x
        self.y = y
        self.z = z



    def add (self,t):
        return  Triple (self.x + t.x, self.y + t.y, self.z + t.z)

    def subtract (self,t):
        return  Triple (self.x - t.x, self.y - t.y, self.z - t.z)

    def cross ( self,t):
        return  Triple (self.y * t.z - self.z * t.y, self.z * t.x - self.x * t.z, x * t.y - self.y * t.x)

    def dot ( self, t):
        return self.x * t.x + self.y * t.y +self.z * t.z

    def length2 (self):
        return self.dot ()

    def normalize (self):
        return self.scale (1.0 / math.sqrt (self.length2 ()))

    def scale ( self,scale):
        return  Triple (self.x * scale, self.y * scale, self.z * scale)




class FractalTerrain:




    def __init__(self, lod, roughness):

        self.blue = RGB(0.0, 0.0, 1.0)
        self.green = RGB(0.0, 1.0, 0.0)
        self.white = RGB(1.0, 1.0, 1.0)

        self.roughness = roughness
        self.divisions = 1 << lod


        self.terrain = np.zeros((self.divisions+1, self.divisions+1), dtype = np.float)

        self.terrain[0][0] = random.random()
        self.terrain[0][self.divisions] = random.random()
        self.terrain[self.divisions][self.divisions] = random.random()
        self.terrain[self.divisions][0] = random.random()


        rough = roughness
        for i in range(lod):

            q = 1 << i
            r = 1 << (lod - i)
            s = r >> 1

            for j in range(0,self.divisions, r):
                for k in range(0, self.divisions, r):
                    self.diamond (j, k, r, rough)
            if (s > 0):
                for j in range(0, self.divisions, s):
                    for k in range( (j + s) % r, self.divisions, r):
                        self.square (j - s, k - s, r, rough)
            rough *= roughness


        self.min = self.max = self.terrain[0][0]
        for i in range(self.divisions):
            for j in range(self.divisions):
                if (self.terrain[i][j] < self.min):
                    self.min = self.terrain[i][j]
                elif (self.terrain[i][j] > self.max):
                    self.max = self.terrain[i][j]






    def diamond (self, x, y, side, scale):
        if (side > 1):
            half = side / 2
            avg = (self.terrain[x][y] + self.terrain[x + side][y] + self.terrain[x + side][y + side] + self.terrain[x][y + side]) * 0.25
            self.terrain[int(x + half)][int(y + half)] = avg + random.random () * scale


    def square ( self, x,  y,  side,  scale):
        half = side / 2
        avg = 0.0
        sum = 0.0
        if (x >= 0):
            avg += self.terrain[x][int(y + half)]
            sum += 1.0

        if (y >= 0):
            avg += self.terrain[int(x + half)][y]
            sum += 1.0

        if (x + side <= self.divisions):
            avg += self.terrain[int(x + side)][int(y + half)]
            sum += 1.0

        if (y + side <= self.divisions):
            avg += self.terrain[int(x + half)][int(y + side)]
            sum += 1.0
        self.terrain[int(x + half)][int(y + half)] = avg / sum + random.random () * scale




    def getAltitude (self, i,  j):
        alt = self.terrain[(int) (i * self.divisions)][(int) (j * self.divisions)]
        return (alt - self.min) / (self.max - self.min)




    def getColor (self,  i,  j):
        a = self.getAltitude (i, j)
        if (a < .5):
            ret_color = self.blue.scale((a-0.0)/0.5)
            ret_color = self.green.subtract(ret_color.r, ret_color.g, ret_color.b)
            ret_color = self.blue.add(ret_color.r,ret_color.g, ret_color.b)
            return ret_color

            #return self.blue.add (self.green.subtract (self.blue.scale ((a - 0.0) / 0.5)))
        else:
            ret_color = self.green.scale((a-0.5)/0.5)
            ret_color = self.white.subtract(ret_color.r, ret_color.g, ret_color.b)
            ret_color = self.green.add(ret_color.r,ret_color.g, ret_color.b)
            return  ret_color
            #return self.green.add (self.white.subtract (self.green.scale ((a - 0.5) / 0.5)))



class Triangle:

    def __init__(self, i0,  j0,  i1,  j1,  i2,  j2):
        i[0] = i0
        i[1] = i1
        i[2] = i2
        j[0] = j0
        j[1] = j1
        j[2] = j2







    def paint(self,canvas):
        for i in range(self.numTriangles):
            xy0 = scrMap[self.triangles[i].i[0]][self.triangles[i].j[0]]
            xy1 = scrMap[self.triangles[i].i[1]][self.triangles[i].j[1]]
            xy2 = scrMap[self.triangles[i].i[2]][self.triangles[i].j[2]]
            dot = - map[self.triangles[i].i[0]][self.triangles[i].j[0]].subtract(loc).normalize().dot(self.triangles[i].n)
            if ((dot > 0.0) and (xy0 != None) and (xy1 != None) and (xy2 != None)):
                x = {xy0.x, xy1.x, xy2.x}
                y = {xy0.y, xy1.y, xy2.y}
                points = [x, y]
                canvas.create_polygon(points, fill="green")
                # g.setColor (triangles[i].color);
                # g.fillPolygon (x, y, 3);

#/* modified lighting computation:
#    ...
#    double shadow = shade[k][l];
#    double lighting = ambient + diffuse * ((dot < 0.0) ? - dot : 0.0) /
#                                  distance2 * shadow;
#*/

class Quaternion:

    def __init__(self,  w,  x,  y,  z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.inv = None

    def inverse (self):
        scale = 1.0 / (self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)
        return Quaternion (self.w * scale, - self.x * scale, - self.y * scale, - self.z * scale)



    def multiply (self,q):
         qx = q.x
         qy = q.y
         qz = q.z
         qw = q.w

         rw = self.w * qw - x * qx - y * qy - z * qz
         rx = w * qx + x * qw + y * qz - z * qy
         ry = w * qy + y * qw + z * qx - x * qz
         rz = w * qz + z * qw + x * qy - y * qx
         return  Quaternion (rw, rx, ry, rz)

    def rotate (self, t):
        if self.inv is None:
            self.inv= self.inverse()
        iw = self.inv.w
        ix = self.inv.x
        iy = self.inv.y
        iz = self.inv.z
        tx = t.x
        ty = t.y
        tz = t.z
        aw = - self.x * tx - self.y * ty - self.z * tz
        ax = self.w * tx + self.y * tz - self.z * ty
        ay = self.w * ty + self.z * tx - self.x * tz
        az = self.w * tz + self.x * ty - self.y * tx
        bx = aw * ix + ax * iw + ay * iz - az * iy
        by = aw * iy + ay * iw + az * ix - ax * iz
        bz = aw * iz + az * iw + ax * iy - ay * ix
        return  Triple (bx, by, bz)



    def newRotation ( r,  x,  y,  z):
        len = math.sqrt (x * x + y * y + z * z)
        sin = math.sin (r / 2.0)
        cos = math.cos (r / 2.0)
        tmp = sin / len
        return Quaternion (cos, x * tmp, y * tmp, z * tmp)

tk = Tk()
tk.title('Test')
canvas_width = 400
canvas_height = 300
main_canvas = Canvas(tk, width=canvas_width, height=canvas_height)
main_canvas.pack()

exaggeration = .7
lod = 5
steps = 1 << lod

map =  np.empty((steps+1,steps+1), dtype = object)
colors =  np.empty((steps+1,steps+1), dtype=object)
terrain = FractalTerrain (lod, .5)

for i in range(steps):
    for j in range(steps):
        x = 1.0 * i / steps
        z = 1.0 * j / steps
        altitude = terrain.getAltitude (x, z)
        map[i][j] =  Triple (x, altitude * exaggeration, z)
        colors[i][j] = terrain.getColor (x, z)


numTriangles = (steps * steps * 2)
triangles = Triangle[numTriangles]
triangle = 0
for i in range(steps):
    for j in range (steps):
        triangles[triangle] =  Triangle (i, j, i + 1, j, i, j + 1)
        triangle += 1
        triangles[triangle] =  Triangle (i + 1, j, i + 1, j + 1, i, j + 1)
        triangle += 1

ambient = .3
diffuse = 4.0

normals =  Triple[steps + 1][steps + 1]
sun =  Triple (3.6, 3.9, 0.6)

for i in range(numTriangles):
    for j in range (3):
        normals[i][j] =  Triple (0.0, 0.0, 0.0)


#compute triangle normals and vertex averaged normals */
for i in range(numTriangles):
    v0 = map[triangles[i].i[0]][triangles[i].j[0]]
    v1 = map[triangles[i].i[1]][triangles[i].j[1]]
    v2 = map[triangles[i].i[2]][triangles[i].j[2]]

    normal = v0.subtract (v1).cross (v2.subtract (v1)).normalize ()
    triangles[i].n = normal
    for j in range(3):
        normals[triangles[i].i[j]][triangles[i].j[j]] = normals[triangles[i].i[j]][triangles[i].j[j]].add (normal)

# compute vertex colors and triangle average colors */
for i in range(numTriangles):
    avg = RGB (0.0, 0.0, 0.0)
    for j in range(3):
        k = triangles[i].i[j]
        l = triangles[i].j[j]
        vertex = map[k][l]
        color = colors[k][l]
        normal = normals[k][l].normalize ()
        light = vertex.subtract (sun)
        distance2 = light.length2 ()
        dot = light.normalize ().dot (normal)
        #lighting = ambient + diffuse * ((dot < 0.0) ? - dot : 0.0) / distance2
        modifier = dot *-1 if dot <0.0 else 0.0
        lighting = ambient + diffuse * modifier / distance2

        color = color.scale (lighting)
        triangles[i].color[j] = color
        avg = avg.add (color)
    triangles[i].color = Color (avg.scale (1.0 / 3.0).toRGB ())

shade = double[steps + 1][steps + 1]
for i in range(steps):
    for j in range(steps):
        shade[i][j] = 1.0
        vertex = map[i][j]
        ray = sun.subtract (vertex)
        distance = steps * math.sqrt (ray.x * ray.x + ray.z * ray.z)
        # step along ray in horizontal units of grid width */

        for place in range(distance):
            sample = vertex.add (ray.scale (place / distance))
            sx = sample.x
            sy = sample.y
            sz = sample.z

            if ((sx < 0.0) or (sx > 1.0) or (sz < 0.0) or (sz > 1.0)):
                break #/* steppd off terrain */
            ground = exaggeration * terrain.getAltitude (sx, sz)
            if (ground >= sy):
                shade[i][j] = 0.0
                break



loc = Triple (0.5, 3.0, -2.0)
rot = Quaternion.newRotation(-.82, 1.0, 0.0, 0.0)
eyeMap =  np.empty((steps+1,steps+1), dtype = object)
scrMap = np.empty((steps+1,steps+1), dtype= tuple)

for i in range(steps):
    for j in range(steps):
        p = map[i][j]
        t = p.subtract(loc)
        r = rot.rotate(t)
        eyeMap[i][j] = r

hither = .1
fov = math.pi / 3
#eyeMap = np.empty((steps + 1,steps + 1))
width = canvas_width
height = canvas_height
scale = width / 2 / math.tan (fov / 2)
for i in range(steps):
    for j in range(steps):
        p = eyeMap[i][j]
        x = p.x
        y = p.y
        z = p.z
        if (z >= hither):
            tmp = scale / z
            pos = ((width / 2 + int((x * tmp))), (height / 2 - int((y * tmp))))
            scrMap[i][j] = pos
        else:
            scrMap[i][j] = None





paint(main_canvas)

tk.update()



