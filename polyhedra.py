from vpython import *
from vpextensions.colors import *
from vpextensions.vectors import *
from vpextensions.triangles import *
from vpextensions.quads import *

phi = (1 + 5**(1/2)) / 2

label_epsilon = 0.25


def handle_label_visibility(poly):
    global label_epsilon

    if not type(poly) is Tetrahedron: #becaues the tetrahedron has labels on its corners
        for i in range(len(poly.labels)):
                try: # because the cube has no triangles
                    centroid = (poly.triangles[i].v0.pos + poly.triangles[i].v1.pos + poly.triangles[i].v2.pos) / 3
                    normal_vector = normal(poly.triangles[i])
                except:
                    try:
                        centroid = (poly.quads[i].v0.pos + poly.quads[i].v1.pos + poly.quads[i].v2.pos + poly.quads[i].v3.pos) / 4
                        normal_vector = normal(poly.quads[i])# Vector from the camera to the centroid of the face
                    except:
                        pass
                
                to_camera = scene.camera.pos - centroid
                
                dot_product = normal_vector.dot(to_camera)

                try:
                    poly.labels[i].visible = (dot_product < -label_epsilon)
                except:
                    pass


class Icosahedron:
    a = 1/2
    b = 1/(2*phi)

    vertices = (
        (0,  0,  0), # because i cant be bothered reducing all the vertices values by 1 lol
        (0,  b,  -a),
        (b,  a,  0 ),
        (-b, a,  0 ),
        (0,  b,  a ),
        (0, -b,  a ),
        (-a, 0,  b ),
        (0,  -b, -a),
        (a,  0,  -b),
        (a,  0,  b ),
        (-a, 0,  -b),
        (b,  -a,  0),
        (-b, -a,  0)
        )
    faces = (
            (vertices[1],  vertices[2],  vertices[3]),  #1
            (vertices[5],  vertices[12], vertices[6]),  #2
            (vertices[1],  vertices[7],  vertices[8]),  #3
            (vertices[4],  vertices[9],  vertices[5]),  #4
            (vertices[4],  vertices[6],  vertices[3]),  #5
            (vertices[11], vertices[9],  vertices[8]),  #6
            (vertices[1],  vertices[3],  vertices[10]), #7
            (vertices[7],  vertices[12], vertices[11]), #8
            (vertices[2],  vertices[8],  vertices[9]),  #9
            (vertices[7],  vertices[10], vertices[12]), #10
            (vertices[4],  vertices[2],  vertices[9]),  #11
            (vertices[12], vertices[10], vertices[6]),  #12
            (vertices[4],  vertices[3],  vertices[2]),  #13
            (vertices[5],  vertices[9],  vertices[11]), #14
            (vertices[3],  vertices[6],  vertices[10]), #15
            (vertices[7],  vertices[11], vertices[8]),  #16
            (vertices[1],  vertices[10], vertices[7]),  #17
            (vertices[4],  vertices[5],  vertices[6]),  #18
            (vertices[1],  vertices[8],  vertices[2]),  #19
            (vertices[5],  vertices[11], vertices[12])  #20
            )
    labels = []
    triangles = []
    quads = []
    weightmap = []
    cylinders = []

    def __init__(self) -> None:
        pass
    
    def draw_shape(ico): 
        face_num = 0

        for face in ico.faces:
            vs = []
            
            col=calculate_color(ico.weightmap,face_num)

            for vertex_coords in face:
                vs.append(vertex(pos=vector(vertex_coords[0]*2, vertex_coords[1]*2, vertex_coords[2]*2), color=col))
            
            centroid = (vs[0].pos + vs[1].pos + vs[2].pos) / 3

            ico.triangles.append(triangle(vs=vs))
            ico.labels.append(label(pos=centroid, text=str(face_num+1), height=15, color=color.black, opacity=0, box=False))
            
            ico.cylinders.append(cylinder(pos=vs[0].pos,axis=sub(vs[1].pos,vs[0].pos),length=distance(vs[0].pos,vs[1].pos),radius=0.02,color=color.black))
            ico.cylinders.append(cylinder(pos=vs[1].pos,axis=sub(vs[2].pos,vs[1].pos),length=distance(vs[1].pos,vs[2].pos),radius=0.02,color=color.black))
            ico.cylinders.append(cylinder(pos=vs[2].pos,axis=sub(vs[0].pos,vs[2].pos),length=distance(vs[2].pos,vs[0].pos),radius=0.02,color=color.black))

            face_num += 1
    

class Dodecahedron:
    a = phi
    b = phi - 1

    vertices = (
                ( 0,  0,  0),
                ( 0,  b,  a),
                ( 0, -b,  a),
                ( 0, -b, -a),
                ( 0,  b, -a),
                ( a,  0,  b),
                (-a,  0,  b),
                (-a,  0, -b),
                ( a,  0, -b),
                ( b,  a,  0),
                (-b,  a,  0),
                (-b, -a,  0),
                ( b, -a,  0),
                ( 1,  1,  1),
                (-1,  1,  1),
                (-1, -1,  1),
                ( 1, -1,  1),
                ( 1, -1, -1),
                ( 1,  1, -1),
                (-1,  1, -1),
                (-1, -1, -1)
            )
    faces = (
                (vertices[13],  vertices[5],  vertices[16], vertices[2],  vertices[1]), #1
                (vertices[16],  vertices[12], vertices[11], vertices[15], vertices[2]), #2
                (vertices[5], vertices[8], vertices[17], vertices[12],  vertices[16]),  #3
                (vertices[2],  vertices[15], vertices[6],  vertices[14], vertices[1]),  #4
                (vertices[13],  vertices[9],  vertices[18], vertices[8],  vertices[5]), #5
                (vertices[14],  vertices[10], vertices[9],  vertices[13], vertices[1]), #6
                (vertices[20],  vertices[11], vertices[12], vertices[17], vertices[3]), #7
                (vertices[15],  vertices[11],  vertices[20], vertices[7], vertices[6]), #8
                (vertices[17],  vertices[8],  vertices[18], vertices[4],  vertices[3]), #9
                (vertices[6], vertices[7], vertices[19], vertices[10],  vertices[14]),  #10
                (vertices[4], vertices[18], vertices[9],  vertices[10], vertices[19]),  #11
                (vertices[4],  vertices[19], vertices[7],  vertices[20], vertices[3]),  #12
            )
    labels = []
    triangles = []
    quads = []
    cylinders = []
    weightmap = []

    def __init__(self) -> None:
        pass
    
    def draw_shape(dod): 
        face_num = 0

        for face in dod.faces:
            vs = []

            col=calculate_color(dod.weightmap,face_num)

            for vertex_coords in face:
                vs.append(vertex(pos=vector(vertex_coords[0], vertex_coords[1], vertex_coords[2]), color=col))
            
            centroid = (vs[0].pos + vs[1].pos + vs[2].pos + vs[3].pos + vs[4].pos) / 5

            quadvs = [vs[0], vs[1], vs[2], vs[3]]
            trivs = [vs[3], vs[4], vs[0]]

            dod.quads.append(quad(vs=quadvs))
            dod.triangles.append(triangle(vs=trivs))
            dod.labels.append(label(pos=centroid, text=str(face_num+1), height=15, color=color.black, opacity=0, box=False))
            
            dod.cylinders.append(cylinder(pos=vs[0].pos,axis=sub(vs[1].pos,vs[0].pos),length=distance(vs[1].pos,vs[0].pos),radius=0.02,color=color.black))
            dod.cylinders.append(cylinder(pos=vs[1].pos,axis=sub(vs[2].pos,vs[1].pos),length=distance(vs[2].pos,vs[1].pos),radius=0.02,color=color.black))
            dod.cylinders.append(cylinder(pos=vs[2].pos,axis=sub(vs[3].pos,vs[2].pos),length=distance(vs[3].pos,vs[2].pos),radius=0.02,color=color.black))
            dod.cylinders.append(cylinder(pos=vs[3].pos,axis=sub(vs[4].pos,vs[3].pos),length=distance(vs[4].pos,vs[3].pos),radius=0.02,color=color.black))
            dod.cylinders.append(cylinder(pos=vs[4].pos,axis=sub(vs[0].pos,vs[4].pos),length=distance(vs[0].pos,vs[4].pos),radius=0.02,color=color.black))

            face_num += 1
            

class Decahedron:
    a = phi
    b = phi - 1
    c = phi + 1

    vertices = (
                ( 0, 0, 0),
                ( 1, 1, 1),
                ( 1,-1,-1),
                (-1, 1, 1),
                (-1,-1,-1),
                ( 0, a, b),
                ( 0,-a,-b),
                ( a, b, 0),
                ( a,-b, 0),
                (-a, b, 0),
                (-a,-b, 0),
                ( 0,-a, c),
                ( 0, a,-c),
            )
    faces = (
                (vertices[1],  vertices[5],  vertices[7],  vertices[12]), #1
                (vertices[9],  vertices[3],  vertices[10], vertices[11]), #2
                (vertices[6],  vertices[2],  vertices[4],  vertices[12]), #3
                (vertices[7],  vertices[8],  vertices[1],  vertices[11]), #4
                (vertices[10], vertices[4],  vertices[9],  vertices[12]), #5
                (vertices[5],  vertices[1],  vertices[3],  vertices[11]), #6
                (vertices[8],  vertices[7],  vertices[2],  vertices[12]), #7
                (vertices[4],  vertices[10], vertices[6],  vertices[11]), #8
                (vertices[3],  vertices[9],  vertices[5],  vertices[12]), #9
                (vertices[2],  vertices[6],  vertices[8],  vertices[11]), #10
            )
    labels = []
    triangles = []
    quads = []
    cylinders = []
    weightmap = []
    dec_offset = 0

    def __init__(self, dec_offset=0) -> None:
        self.dec_offset = dec_offset
    
    def draw_shape(dec): 
        face_num = 0

        for face in dec.faces:
            vs = []

            col=calculate_color(dec.weightmap,face_num)

            for vertex_coords in face:
                vs.append(vertex(pos=vector(vertex_coords[0], vertex_coords[1], vertex_coords[2]), color=col))
            
            centroid = (vs[0].pos + vs[1].pos + vs[2].pos + vs[3].pos) / 4

            quadvs = [vs[0], vs[1], vs[3], vs[2]]

            dec.quads.append(quad(vs=quadvs))
            dec.labels.append(label(pos=centroid, text=str((face_num+1)*(10**dec.dec_offset)), height=15, color=color.black, opacity=0, box=False))
            
            dec.cylinders.append(cylinder(pos=vs[0].pos,axis=sub(vs[1].pos,vs[0].pos),length=distance(vs[1].pos,vs[0].pos),radius=0.03,color=color.black))
            dec.cylinders.append(cylinder(pos=vs[0].pos,axis=sub(vs[2].pos,vs[0].pos),length=distance(vs[2].pos,vs[0].pos),radius=0.03,color=color.black))
            dec.cylinders.append(cylinder(pos=vs[2].pos,axis=sub(vs[3].pos,vs[2].pos),length=distance(vs[3].pos,vs[2].pos),radius=0.03,color=color.black))

            face_num += 1


class Octahedron:
    vertices =  (
                ( 0,   0,   0),
                ( 0,   0,   1),
                ( 0,   1,   0),
                ( 1,   0,   0),
                ( 0,   0,  -1),
                ( 0,  -1,   0),
                (-1,   0,   0),
                )
    faces = (
            (vertices[1], vertices[2], vertices[3]), #1
            (vertices[6], vertices[5], vertices[4]), #2
            (vertices[3], vertices[4], vertices[5]), #3
            (vertices[6], vertices[2], vertices[1]), #4
            (vertices[6], vertices[4], vertices[2]), #5
            (vertices[1], vertices[3], vertices[5]), #6
            (vertices[1], vertices[5], vertices[6]), #7
            (vertices[4], vertices[3], vertices[2]), #8
            )
    labels = []
    triangles = []
    quads = []
    cylinders = []
    weightmap = []

    def __init__(self) -> None:
        pass
    
    def draw_shape(oct): 
        face_num = 0

        for face in oct.faces:
            vs = []
            
            col=calculate_color(oct.weightmap,face_num)

            for vertex_coords in face:
                vs.append(vertex(pos=vector(vertex_coords[0]*2, vertex_coords[1]*2, vertex_coords[2]*2), color=col))
            
            centroid = (vs[0].pos + vs[1].pos + vs[2].pos) / 3

            oct.triangles.append(triangle(vs=vs))
            oct.labels.append(label(pos=centroid, text=str(face_num+1), height=15, color=color.black, opacity=0, box=False))
            
            oct.cylinders.append(cylinder(pos=vs[0].pos,axis=sub(vs[1].pos,vs[0].pos),length=distance(vs[0].pos,vs[1].pos),radius=0.02,color=color.black))
            oct.cylinders.append(cylinder(pos=vs[1].pos,axis=sub(vs[2].pos,vs[1].pos),length=distance(vs[1].pos,vs[2].pos),radius=0.02,color=color.black))
            oct.cylinders.append(cylinder(pos=vs[2].pos,axis=sub(vs[0].pos,vs[2].pos),length=distance(vs[2].pos,vs[0].pos),radius=0.02,color=color.black))

            face_num += 1


class Cube: #should i rename to Hexahedron?
    vertices =  (
                ( 1,  1,  1),
                ( 1,  1, -1),
                ( 1, -1,  1),
                ( 1, -1, -1),
                (-1,  1,  1),
                (-1,  1, -1),
                (-1, -1,  1),
                (-1, -1, -1),
                )
    faces = (
            (vertices[0], vertices[1], vertices[3], vertices[2]), #1
            (vertices[4], vertices[5], vertices[1], vertices[0]), #2
            (vertices[5], vertices[7], vertices[3], vertices[1]), #3
            (vertices[0], vertices[2], vertices[6], vertices[4]), #4
            (vertices[2], vertices[3], vertices[7], vertices[6]), #5
            (vertices[6], vertices[7], vertices[5], vertices[4]), #6
            )
    labels = []
    triangles = []
    quads = []
    cylinders = []
    weightmap = []

    def __init__(self) -> None:
        pass
    
    def draw_shape(cube): 
        face_num = 0

        for face in cube.faces:
            vs = []
            
            col=calculate_color(cube.weightmap,face_num)

            for vertex_coords in face:
                vs.append(vertex(pos=vector(vertex_coords[0], vertex_coords[1], vertex_coords[2]), color=col))
            
            centroid = (vs[0].pos + vs[1].pos + vs[2].pos + vs[3].pos) / 4

            cube.quads.append(quad(vs=vs))
            cube.labels.append(label(pos=centroid, text=str(face_num+1), height=15, color=color.black, opacity=0, box=False))
            
            cube.cylinders.append(cylinder(pos=vs[0].pos,axis=sub(vs[1].pos,vs[0].pos),length=distance(vs[0].pos,vs[1].pos),radius=0.03,color=color.black))
            cube.cylinders.append(cylinder(pos=vs[1].pos,axis=sub(vs[2].pos,vs[1].pos),length=distance(vs[1].pos,vs[2].pos),radius=0.03,color=color.black))
            cube.cylinders.append(cylinder(pos=vs[2].pos,axis=sub(vs[3].pos,vs[2].pos),length=distance(vs[2].pos,vs[3].pos),radius=0.03,color=color.black))
            cube.cylinders.append(cylinder(pos=vs[3].pos,axis=sub(vs[0].pos,vs[3].pos),length=distance(vs[3].pos,vs[0].pos),radius=0.03,color=color.black))

            face_num += 1


class Tetrahedron:
    vertices =  (
                [ 1,  1, -1],
                [-1, -1, -1],
                [ 1, -1,  1],
                [-1,  1,  1],
                )
    faces = (
            (vertices[2], vertices[1], vertices[0]), #1
            (vertices[3], vertices[1], vertices[0]), #2
            (vertices[3], vertices[2], vertices[0]), #3
            (vertices[3], vertices[2], vertices[1]), #4
            )
    labels = []
    triangles = []
    quads = []
    cylinders = []
    weightmap = []

    def __init__(self) -> None:
        pass
    
    def draw_shape(tet): 
        cols = []
        vert_num = 0
        for vert in tet.vertices:
            pos = vector(vert[0] * 1.5, vert[1] * 1.5, vert[2] * 1.5)
            tet.labels.append(label(pos=pos, text=str(vert_num+1), height=15, color=color.black, opacity=0, box=False))
            vert.append(calculate_color(tet.weightmap,vert_num))
            vert_num += 1

        face_num = 0

        for face in tet.faces:
            vs = []

            for vert in face:
                vs.append(vertex(pos=vector(vert[0]*2, vert[1]*2, vert[2]*2), color=vert[3]))

            tet.triangles.append(triangle(vs=vs))
            
            tet.cylinders.append(cylinder(pos=vs[0].pos,axis=sub(vs[1].pos,vs[0].pos),length=distance(vs[0].pos,vs[1].pos),radius=0.02,color=color.black))
            tet.cylinders.append(cylinder(pos=vs[1].pos,axis=sub(vs[2].pos,vs[1].pos),length=distance(vs[1].pos,vs[2].pos),radius=0.02,color=color.black))
            tet.cylinders.append(cylinder(pos=vs[2].pos,axis=sub(vs[0].pos,vs[2].pos),length=distance(vs[2].pos,vs[0].pos),radius=0.02,color=color.black))

            face_num += 1

