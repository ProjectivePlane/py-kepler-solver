#!/usr/bin/python

import solve

ecc=1.5
N=2000
M=2000
x=[]
y=[]
for n in range(N,2*N):
    x.append(n*1.0/M)
    y.append(solve.solve_for_hyperbolic_anomaly((n*1.0/M),ecc))

fh=open('hyperbolicanomaly.gnuplot','w')
for n in range(N):
    fh.write(str(x[n]))
    fh.write(" ")
    fh.write(str(y[n]))
    fh.write("\n")

fh.close()
