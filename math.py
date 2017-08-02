import math

def Volume(r):
    V = (4/3) * (math.pi) * (r)**3
    return V
print (Volume (8))


def Area(r):
    A = (4) * (math.pi) * r**2
    return A
print (Area (8))


def Unitcost(d,TC):
    A = (math.pi) * d**2 / 4
    UC = TC/A
    return UC
print (Unitcost(8, 40))
