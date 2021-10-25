import j3d.matrix as jm
import j3d.vector as jv
import j3d.util as ju
import math

class j3d_light:

    def __init__(self,dir):
        self.dir = dir
        self.eye = [0, 0, 0, 1]

        self.dir_internal = 0 # I set this to 0 maybe it does not need to be set at all...
        self.eye_internal = 0

        work1 = [0, 0, 0, 0]
        work2 = [0, 0, 0, 0]

    def transform(matrix):
        inverse = jm.j3d_matrix_invert_simple(matrix)

        self.dir_internal = jm.j3d_matrix_multiply([self.dir], inverse)[0]
        self.eye_internal = jm.j3d_matrix_multiply([self.eye], inverse)[0]


    def light_face(normal, center, material):
        if (material.static):
            return material.static
        else:
            # ambient component

            r = material.ambient[0]
            g = material.ambient[1]
            b = material.ambient[2]

            # diffuse component

            diff = jv.j3d_vector_dot(normal, dir_internal)

            if (diff > 0):
                r += material.diffuse[0] * diff
                g += material.diffuse[1] * diff
                b += material.diffuse[2] * diff

            # specular component

            if (normal != None and center != None):
                v1 = jv.j3d_vector_subtract(center, eye_internal, work1)
                dot = jv.j3d_vector_dot(v1, normal)
                v2 = jv.j3d_vector_multiply(normal, -2 * dot, work2)
                v3 = jv.j3d_vector_add(v1, v2, work1)
                v4 = jv.j3d_vector_normalize(v3, work1)

                spec = jv.j3d_vector_dot(v4, dir_internal)

                if (spec > 0):
                    spec = math.pow(spec, material.phong)
                    r += material.specular[0] * spec
                    g += material.specular[1] * spec
                    b += material.specular[2] * spec

            # generate HTML color

            return ju.j3d_util_rgbcolor(r * 256, g * 256, b * 256)


    def light_model(model, matrix):
        this.transform(matrix)

        length = model.faces.j3d_length

        if (length == null):
            length = model.faces.length

        for i in range(length):
            face = model.faces[i]
            face.color = self.light_face(model.normals[face.normal], model.centers[face.center], face.material)

        return model
