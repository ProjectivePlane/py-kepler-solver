#!/usr/bin/python

import math

def f(E,e,M):
    return E-e*math.sin(E)-M

def solve_for_eccentric_anomaly(M,e,accuracy=0.000001):
    if e<=0.8:
        oldE=M
    else:
        oldE=math.pi
    newE=0
    while abs(f(oldE,e,M))>=accuracy:
        newE=oldE-(f(oldE,e,M)/(1-e*math.cos(oldE)))
        oldE=newE
    return newE
