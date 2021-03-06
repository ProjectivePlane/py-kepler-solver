#!/usr/bin/python

import math

def f(E,e,M):
    return E-e*math.sin(E)-M

def hf(H,e,M):
    return e*math.sinh(H)-H-M

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

def solve_for_hyperbolic_anomaly(M,e,accuracy=0.000001):
    oldH=M
    newH=0
    while abs(hf(oldH,e,M)>=accuracy):
        newH=oldH-(hf(oldH,e,M)/(e*math.cosh(oldH)-1))
        oldH=newH
    return newH

def solve_for_mean_anomaly(E,e):
    return E-e*math.sin(E)

def solve_for_hyperbolic_mean_anomaly(H,e):
    return e*math.sinh(H)-H
