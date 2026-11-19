import math

d_model = 4
pos = 1
i = 0
a = 2*1
b = a/d_model
c = 10000**a
d = pos/b
sin = math.sin(d)
cos = math.cos(d)

print(sin)
print(cos)