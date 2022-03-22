import math


def main(z):
    if z < 89:
        res = ((math.cos(15*z**3)**7)/92)-81
    elif 89 <= z < 172:
        res = (1 + 80*z + 50*z**3)**2
    elif 172 <= z < 206:
        res = (48*((z**3/88)+(z*z)+z)**4) + (((1+z/45)**0.5)**3) + z*z
    elif 206 <= z < 268:
        res = (34*z*z)**7+81*(4-z*z-49*z**3)**4+z**5
    elif z >= 268:
        res = 21*math.atan(z)**2
    return res