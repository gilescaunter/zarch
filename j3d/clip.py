import j3d.matrix as jm
import  j3d.vector as jv

def j3d_clip(planes):
    this.planes = planes

    planes_internal

    def transform (matrix):
        transpose = jm.j3d_matrix_transpose(matrix)
        planes_internal = jm.j3d_matrix_multiply(planes, transpose)


    def clip_indices(indices, vertices, matrix, mask):
        if (mask is None):
            mask = 0xffffffff

        vertices0 = vertices[0]
        vertices1 = vertices[1]
        thresh = vertices0.length

        for i in range (indices.length > 0 and i < planes_internal.length):
            plane = planes_internal[i]

            if (mask & 1 << i):
                new_indices = []

                index = indices[indices.length - 1]
                vertex = vertices0[index] if index < thresh else vertices1[index - thresh]
                dot = jv.j3d_vector_dot(vertex, plane)

                for j in range(indices.length):

                    new_index = indices[j]
                    new_vertex = vertices0[new_index] if new_index < thresh else vertices1[new_index - thresh]
                    new_dot = jv.j3d_vector_dot(new_vertex, plane)

                    if (new_dot > 0 and dot <= 0 or new_dot <= 0 and dot > 0):

                        new_indices.push(thresh + vertices1.j3d_length)
                        jv.j3d_vector_blend(vertex, new_vertex, dot / (dot - new_dot), vertices1[vertices1.j3d_length])
                        vertices1.j3d_length += 1


                    if (new_dot <= 0):
                        new_indices.push(new_index)

                    index = new_index
                    vertex = new_vertex
                    dot = new_dot


                indices = new_indices



        return indices


    def clip_model(model, matrix, mprime):
        if (mprime is None):
            mprime = {vertices: []}


    mprime.vertices[0] = model.vertices[0]

    if (mprime.vertices[1] == null or mprime.vertices[1].length < model.faces.length * planes.length):
        mprime.vertices[1] = j3d_util_make2darray(model.faces.length * planes.length, 4)

    mprime.vertices[1].j3d_length = 0

    mprime.normals = model.normals
    mprime.centers = model.centers

    if (mprime.faces == null or mprime.faces.length < model.faces.length):
        mprime.faces = j3d_util_makeobjectarray(model.faces.length)

    # mprime.faces.j3d_length = 0;

    mprime.bias = model.bias

    this.transform(matrix)

    length = 0

    for i in range(model.faces.length):
        face = model.faces[i]

        if (face.clip == 0):
            fprime = mprime.faces[length]

            fprime.indices = face.indices
            fprime.material = face.material
            fprime.normal = face.normal
            fprime.center = face.center
            fprime.clip = face.clip
            fprime.cull = face.cull
            fprime.bias = face.bias

        else:
            iprime = this.clip_indices(face.indices, mprime.vertices, face.clip);

            if (iprime.length > 0):
                fprime = mprime.faces[length]

                fprime.indices = iprime
                fprime.material = face.material
                fprime.normal = face.normal
                fprime.center = face.center
                fprime.clip = face.clip
                fprime.cull = face.cull
                fprime.bias = face.bias

        length += 1
    mprime.faces.j3d_length = length

    return mprime

