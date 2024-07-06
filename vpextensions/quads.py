from vpython import quad

def normal(q:quad): # ASSUMES ALL 4 POINTS ARE COPLANAR
    return (q.v1.pos-q.v0.pos).cross(q.v2.pos-q.v1.pos).norm()