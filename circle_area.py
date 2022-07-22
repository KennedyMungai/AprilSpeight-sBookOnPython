#!/usr/bin/python3
import math as m

def circleArea():
    radius = float(input("Radius: "))
    radiusSqr = m.pow(radius, 2)
    area = m.pi * radiusSqr
    return area

area = circleArea()
print(area)