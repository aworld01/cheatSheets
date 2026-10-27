import math

i = 0
pos = 1
d_model = 4

sin = math.sin(pos/(10000**(i/d_model)))
cos = math.cos(pos/(10000**(i/d_model)))

print(sin)
print(cos)