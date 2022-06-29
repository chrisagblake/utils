import math

def deg_to_rad(v):
    return v * math.pi / 180

def rad_to_deg(v):
    return v * 180 / math.pi

def kn_to_ms(v):
    return v * 1852 / 3600

def ms_to_kn(v):
    return v * 3600 / 1852

def polar_to_cart(speed, angle):
    """
    Convert a speed, angle in polar coordinates into 
    cartesian components of speed

    angle is in radians clockwise from y axis
    """

    x = speed * math.sin(angle)
    y = speed * math.cos(angle)
    return x, y

