import math
import constants as c
import j3d.vector as jv
import j3d.util as ju

lander_ground_size = 32
lander_ground_mask = lander_ground_size - 1
lander_ground_model_size = 12
lander_ground_vscale = 8

lander_ground_pad_x = 14
lander_ground_pad_z = 14

lander_ground_range = (lander_ground_model_size - 1) / 2

def lander_ground_make_pad_alt(alt, x, z):
    avg = 0

    for ox in range(4):
        for oz in range(4):
            avg += alt[x + ox][z + oz];

    avg /= 25;

    if (avg < 0.3):
        avg = 0.3;

    for ox in range(4):
        for oz in range(4):
            alt[x + ox][z + oz] = avg


def lander_ground_make_pad_mat(mat, x, z):
    for ox in range(4):
        for oz in range(4):
            grey = (math.random() + 3.0) / 8.0;

            mat[x + ox][z + oz] = {static: lander_light.light_face([0.0, -1.0, 0.0, 0.0], null,
                                                                   {ambient: [0, 0, 0], diffuse: [grey, grey, grey],
                                                                    specular: [0, 0, 0], phong: 0.0})};


def lander_ground_make(size):
    # build altitude
    alt = [[0] * size for i in range(size)]
    alt[0][0] = 0.0


    for len in range(c.size, len > 1, len / 2):
        for x in range(0, c.size, len):
            for y in range(0, c.size, len):
                v0 = alt[x][y]
                v1 = alt[(x + len) % size][y]
                v2 = alt[x][(y + len) % size]
                v3 = alt[(x + len) % size][(y + len) % size]

                alt[x + len / 2][y] = (v0 + v1) / 2 + (math.random() - 0.5) * len / lander_ground_vscale
                alt[x][y + len / 2] = (v0 + v2) / 2 + (math.random() - 0.5) * len / lander_ground_vscale
                alt[x + len / 2][y + len / 2] = (v0 + v1 + v2 + v3) / 4 + (math.random() - 0.5) * len / lander_ground_vscale



    # clip to sea level

    for x in range(size):
        for y in range(size):
            if (alt[x][y] < 0):
                alt[x][y] = 0


    #lander_ground_make_pad_alt(alt, lander_ground_pad_x, lander_ground_pad_z);

    # build normals and centers
    nor = ju.j3d_util_make2darray(size, size)
    cen = ju.j3d_util_make2darray(size, size)

    for i in range(size):
        for j in range(size):
            a0 = alt[i][j];
            a1 = alt[(i + 1) % size][j]
            a2 = alt[i][(j + 1) % size]
            a3 = alt[(i + 1) % size][(j + 1) % size]

            nor[i][j] = jv.j3d_vector_normalize(jv.j3d_vector_cross([1, a0 - a1, 0, 0], [0, a0 - a2, 1, 0]))
            cen[i][j] = -(a0 + a1 + a2 + a3) / 4


    # choose colors

    lander_light.transform(jm.j3d_matrix_identity())

    mat = ju.j3d_util_make2darray(size, size)
    tre = ju.j3d_util_make2darray(size, size)

    for x in range(size):
        for z in range(size):
            a0 = alt[x][z]
            a1 = alt[(x + 1) % size][z]
            a2 = alt[x][(z + 1) % size]
            a3 = alt[(x + 1) % size][(z + 1) % size]

            if (a0 <= 0 and a1 <= 0 and a2 <= 0 and a3 <= 0):
                r = (math.random() + 1.0) / 16.0
                g = (math.random() + 1.0) / 16.0
                b = (math.random() + 1.0) / 2.0

                mat[x][z] = {ambient: [0, 0, 0], diffuse: [r, g, b], specular: [0.8, 0.8, 0.8], phong: 4.0}
                tre[x][z] = null

            else:
                tone = math.random()

                r = tone
                g = 1.0 - tone / 4.0
                b = 0.0

                mat[x][z] = {static: lander_light.light_face(nor[x][z], null,
                                                             {ambient: [0, 0, 0], diffuse: [r, g, b], specular: [0, 0, 0],
                                                              phong: 0.0})}
                if math.random() > 0.95:
                    tre[x][z] = math.random() * math.PI * 2
                else:
                    tre[x][z] = null

                #tre[x][z] = math.random() > 0.95 ? math.random() * math.PI * 2: null

    lander_ground_make_pad_mat(mat, lander_ground_pad_x, lander_ground_pad_z)

    return {altitude: alt, materials: mat, normals: nor, centers: cen, trees: tre}


def lander_ground_make_model(size):
    size2 = (size + 1) * (size + 1)
    model = {}
    model['vertices'] = [[0] * size2 for i in range(size2)]
    model['normals'] =  [[0, -1, 0, 0]]
    model['centres'] = [[0] * size2 for i in range(size2)]
    model['faces'] = [[0] * size2 for i in range(size2)]

    for x in range (size+1):
        for z in range(size+1):
            index1 = x + z * (size + 1)
            model['vertices'][0][index1] = [x, 0, z, 1]

    for x in range (size):
        for z in range(size):
            index1 = x + z * size
            model['centres'][0][index1] = [x + 0.5, 0, z + 0.5, 1]

            indices_arr = [0] * 4
            indices = {}
            indices['indices'] = indices_arr
            indices['indices'][0] = x + z * (size + 1)
            indices['indices'][1] = x + (z + 1) * (size + 1)
            indices['indices'][2] = (x + 1) + (z + 1) * (size + 1)
            indices['indices'][3] = (x + 1) + z * (size + 1)
            indices['normal'] = 0
            indices['center'] = x + z * size
            model['faces'][index1] = indices

            clip = 0

            if (x == size - 1):
                clip |= 1
            if (z == size - 1):
                clip |= 2
            if (x == 0):
                clip |= 4
            if (z == 0):
                clip |= 8

            indices['clip'] = clip
            indices['cull'] = False

            model['faces'][index1] = indices


    return model

    lander_ground_model = lander_ground_make_model(lander_ground_model_size)

    lander_ground_prev_x = 1000000;
    lander_ground_prev_z = 1000000;

def lander_ground_setup_model(x, z):
    x = math.floor(x - lander_ground_model_size / 2 + 0.5)
    z = math.floor(z - lander_ground_model_size / 2 + 0.5)

    if (x != lander_ground_prev_x or z != lander_ground_prev_z):
        lander_ground_prev_x = x
        lander_ground_prev_z = z

        vertices = lander_ground_model.vertices[0]

        for i in range(lander_ground_model_size + 1):
            altitude = lander_ground.altitude[x + i & lander_ground_mask]

            for j in range(lander_ground_model_size + 1):
                vertices[i + j * (lander_ground_model_size + 1)][1] = - altitude[z + j & lander_ground_mask];


        centers = lander_ground_model.centers
        faces = lander_ground_model.faces

        for i in range(lander_ground_model_size):
            ground_centers = lander_ground.centers[x + i & lander_ground_mask]
            ground_materials = lander_ground.materials[x + i & lander_ground_mask]

            for j in range(lander_ground_model_size):
                centers[i + j * lander_ground_model_size][1] = ground_centers[z + j & lander_ground_mask]

                faces[i + j * lander_ground_model_size].material = ground_materials[z + j & lander_ground_mask]


def lander_ground_setup_clip(x, z):
    lander_clip.planes[0][3] = -(x + lander_ground_range)
    lander_clip.planes[1][3] = -(z + lander_ground_range)
    lander_clip.planes[2][3] = (x - lander_ground_range)
    lander_clip.planes[3][3] = (z - lander_ground_range)


def lander_ground_init_map():
    scale = 64 / lander_ground_size

    for x in range(lander_ground_size):
        for z in range(lander_ground_size):
            static = lander_ground.materials[x][z].static

        if static is None:
            static = "rgb(0, 0, 128)"

        map_ctx.fillStyle = static
        map_ctx.fillRect(x * scale, (lander_ground_size - 1 - z) * scale, scale, scale)



def lander_ground_matrix(x, z):
    x = math.floor(x - lander_ground_range)
    z = math.floor(z - lander_ground_range)

    return jm.j3d_matrix_translate(x, 0, z)



def lander_ground_height(x, z):
    xt = math.floor(x)
    zt = math.floor(z)

    xf = x - xt
    zf = z - zt

    a0 = - lander_ground.altitude[xt & lander_ground_mask][zt & lander_ground_mask]
    a1 = - lander_ground.altitude[xt + 1 & lander_ground_mask][zt & lander_ground_mask]
    a2 = - lander_ground.altitude[xt & lander_ground_mask][zt + 1 & lander_ground_mask]
    a3 = - lander_ground.altitude[xt + 1 & lander_ground_mask][zt + 1 & lander_ground_mask]

    return (a0 * (1 - xf) + a1 * xf) * (1 - zf) + (a2 * (1 - xf) + a3 * xf) * zf

def lander_ground_draw(cam):
    lander_ground_setup_model(lander_ship.p[0], lander_ship.p[2])
    lander_ground_setup_clip(lander_ship.p[0], lander_ship.p[2])

    mat = lander_ground_matrix(lander_ship.p[0], lander_ship.p[2])

    lander_ground_model1 = lander_clip.clip_model(lander_ground_model, mat, lander_ground_model1)
    lander_light.light_model(lander_ground_model1, mat);
    lander_ground_model2 = jm.j3d_model_multiply(lander_ground_model1, jm.j3d_matrix_multiply(mat, cam), lander_ground_model2)
    lander_ground_model3 = jm.j3d_model_dehomogenize(lander_ground_model2, lander_ground_model3)

    lander_sort.add_model(lander_ground_model3, 0)
