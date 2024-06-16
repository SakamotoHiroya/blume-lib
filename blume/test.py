import encode
import decode
import output

import matplotlib.pyplot as plt
import numpy as np
import math

distances = output.get_distances()

x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []

for distance in distances:
    x1.append(distance[0]);
    x2.append(distance[0]);
    x3.append(distance[0]);
    y1.append(distance[1][0] / 10 + 0.1)
    y2.append(distance[1][1] * 0.075 + 0.02)
    y3.append(distance[1][2] * 0.05 - 0.05)

degree = 300
coefficients = np.polyfit(x1, y1, degree)
polynomial = np.poly1d(coefficients)
y1_fit = polynomial(x1)

coefficients = np.polyfit(x2, y2, degree)
polynomial = np.poly1d(coefficients)
y2_fit = polynomial(x2)

coefficients = np.polyfit(x3, y3, degree)
polynomial = np.poly1d(coefficients)
y3_fit = polynomial(x3)


print(decode.decode(x1, y1))
print(decode.decode(x2, y2))
print(decode.decode(x3, y3))



# x, y = encode.encode_wave([0x0F, 0xFF, 0xFF])
# print(decode.decode(x, y))

