from vpython import triangle


def normal(t:triangle):
    return (t.v1.pos-t.v0.pos).cross(t.v2.pos-t.v1.pos).norm()