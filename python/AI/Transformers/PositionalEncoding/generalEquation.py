"""
if i = 0:
    denominators:
        1 = 10000**(i/d_model)

    sin = 0.8414709848078965
    cos = 0.5403023058681398

if i = 2:
    denominators:
        100 = 10000**(i/d_models)
"""
import math

i = 0
pos = 1
d_model = 4

a = i/d_model
b = 10000**a
print(b)

c = pos/b
print(c)

sin = math.sin(c)
cos = math.cos(c)

print(sin)
print(cos)