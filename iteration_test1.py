# x^2-a=0, compute x by a
import random
# a=input("input a:")
a=114
a=float(a)
x1=random()
x2=x1
while True:
    x2=0.5*(x1+a/x1)
    if abs(x2-x1)<0.001:
        break
    x1=x2
print(f"if a={a}, x={x2}")

