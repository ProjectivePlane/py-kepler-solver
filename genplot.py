#!/usr/bin/python

import solve

ecc=0.65
N=2000
M=200
x=[]
y=[]
for n in range(0,N):
    x.append(n*1.0/M)
    y.append(solve.solve_for_eccentric_anomaly((n*1.0/M),ecc))

fh=open('anomaly.gnuplot','w')
for n in range(N):
    fh.write(str(x[n]))
    fh.write(" ")
    fh.write(str(y[n]))
    fh.write("\n")

fh.close()
