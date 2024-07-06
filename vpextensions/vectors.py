from numpy import *
from vpython import vector


def normal(a:vector,b:vector,c:vector):
    return (b-a).cross(c-b).norm()

def add(v1,v2):
    return vector(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)

def sub(v1,v2):
    return vector(v1.x-v2.x, v1.y-v2.y, v1.z-v2.z)

def distance(v1,v2):
    return sqrt((v2.x-v1.x)**2 + (v2.y-v1.y)**2 + (v2.z-v1.z)**2)