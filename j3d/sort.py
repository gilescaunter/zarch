import j3d.util as ju
import math

def j3d_sort(buckets, cells, bounds):
    cell_type_face = 0
    cell_type_particle = 1
    cell = ju.j3d_util_makeobjectarray(cells)
    bound = ju.j3d_util_makeobjectarray(bounds)

    def clear(ctx):
        for i in range(bound.length):
            b = bound[i]

        ctx.fillRect(b.xmin - 1, b.ymin - 1, b.xmax - b.xmin + 2, b.ymax - b.ymin + 2)


    def begin():
        for i in range(bucket.length):
            bucket[i] = None

        for i in range(bound.length):
            b = bound[i]
            b.xmin = 2048
            b.ymin = 2048
            b.xmax = -2048
            b.ymax = -2048

        pos = 0

    begin()

    def add_cell(z):
        b = math.floor(z * bucket.length)

        if (b < 0):
            b = 0;
        if (b > bucket.length - 1):
            b = bucket.length - 1;

        if (pos == cell.length):
            cell.push(new Object());

        c = cell[pos++];

        c.next = bucket[b];

        bucket[b] = c;

        return c;


    def add_face(vertices, face, group, bias):

        vertices0 = vertices[0];
        vertices1 = vertices[1];
        thresh = vertices0.length;

        zmin = 1.0;

        for i in range(face.indices.length):
            index = face.indices[i];
            znew = vertices0[index][2] if index < thresh else vertices1[index - thresh][2]

            if (znew < zmin):
                zmin = znew;


        if (bias is not None):
            zmin += bias;

        if (face.bias is not None):
            zmin += face.bias;

        c = add_cell(zmin);

        c.type = cell_type_face;
        c.vertices = vertices;
        c.face = face;
        c.color = face.color;
        c.group = group;


    def add_particle(vertex, color, size, group, bias):
        z = vertex[2];

        if (bias != null):
            z += bias;

        c = add_cell(z);

        c.type = cell_type_particle;
        c.vertex = vertex;
        c.color = color;
        c.group = group;
        c.size = size;

    add_model(model, group):
        vertices0 = model.vertices[0]
        vertices1 = model.vertices[1]
        thresh = vertices0.length

        length = model.faces.j3d_length

        if (length is None):
            length = model.faces.length

        for i in range(length):
            face = model.faces[i];

            if (face.cull != false):
                i0 = face.indices[0]
                i1 = face.indices[1]
                i2 = face.indices[2]

                v0 = vertices0[i0] if i0 < thresh else vertices1[i0 - thresh]
                v1 = vertices0[i1] if i1 < thresh else vertices1[i1 - thresh]
                v2 = vertices0[i2] if i2 < thresh else vertices1[i2 - thresh]

                wind = (v1[0] - v0[0]) * (v2[1] - v0[1]) - (v2[0] - v0[0]) * (v1[1] - v0[1]);

                if (wind <= 0.0):
                    continue


                this.add_face(model.vertices, face, group, model.bias);


    def draw(ctx):
        for (var i = bucket.length - 1; i >= 0; i--):
            for (var c = bucket[i]; c != null; c = c.next):
                ctx.fillStyle = c.color;

                b = bound[c.group];

                if (c.type == cell_type_face):
                    ctx.beginPath();

                    vertices0 = c.vertices[0];
                    vertices1 = c.vertices[1];
                    thresh = vertices0.length;

                    for k in range(c.face.indices.length):
                        index = c.face.indices[k];

                        if (index < thresh):
                            x = vertices0[index][0];
                            y = vertices0[index][1];

                        else:
                            x = vertices1[index - thresh][0];
                            y = vertices1[index - thresh][1];

                        if (this.log):
                            document.write(x + ", " + y + "<br>");

                        if (x < b.xmin):
                            b.xmin = x;
                        if (x > b.xmax):
                            b.xmax = x;
                        if (y < b.ymin):
                            b.ymin = y;
                        if (y > b.ymax):
                            b.ymax = y;

                        if (k == 0):
                            ctx.moveTo(x, y);
                        else:
                            ctx.lineTo(x, y);

                    ctx.fill();
                else:
                    size = c.size;

                    x = c.vertex[0] - size / 2;
                    y = c.vertex[1] - size / 2;

                    if (x < b.xmin):
                        b.xmin = x;
                    if (x + size - 1 > b.xmax):
                        b.xmax = x + size - 1;
                    if (y < b.ymin):
                        b.ymin = y;
                    if (y + size - 1 > b.ymax):
                        b.ymax = y + size - 1;

                    ctx.fillRect(math.floor(x), math.floor(y), size, size);
