import math

def kts_to_ms(v):
    return v * 1852 / 3600

def ms_to_kts(v):
    return v * 3600 / 1852

def kmh_to_ms(v):
    return v / 3.6

def ms_to_kmh(v):
    return v * 3.6

def nm_to_km(d):
    return d * 1.852

def km_to_nm(d):
    return d / 1.852

def rad_to_deg(v):
    return v * 180 / math.pi

def deg_to_rad(v):
    return v * math.pi / 180

def lim_pi(v):
    """
    Limit a number between -pi/pi
    """
    while v < -math.pi:
        v += 2 * math.pi
    while v > math.pi:
        v -= 2 * math.pi
    return v

def lim_2pi(v):
    """
    Limit a number between 0/2pi
    """
    while v < 0
        v += 2 * math.pi
    while v > 2 * math.pi:
        v -= 2 * math.pi
    return v

def lim_180(v):
    """
    Limit a angle in degrees between -180 and 180
    """
    while v < -180:
        v += 360
    while v > 180:
        v -= 360
    return v

def lim_360(v):
    """
    Limit a angle in degrees between 0 and 360
    """
    while v < 0:
        v += 360
    while v > 360:
        v -= 360
    return v

def polar_to_cart(length, angle):
    """
    Convert a length, angle in polar coordinates into 
    cartesian components

    angle is in radians clockwise from y axis
    """
    x = length * math.sin(angle)
    y = length * math.cos(angle)
    return x, y

def cart_to_polar(x, y):
    """
    Convert a vector in cartesian components into
    polar coordinates

    angle is in radians, clockwise from the y axis between +-pi
    """
    length = math.sqrt(x**2 + y**2)
    if y == 0:
        if x > 0:
            angle = math.pi / 2
        else:
            angle = -math.pi / 2
    else:
        angle = math.atan(x / y)
        if y < 0:
            if x > 0:
                angle += math.pi
            else:
                angle -= math.pi
    return length, angle

