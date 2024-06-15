import encode
import decode
import output

import matplotlib.pyplot as plt
import numpy as np
import math

distances = output.get_distances()

x = []
y1 = []
y2 = []
y3 = []

for distance in distances:
    x.append(distance[0]);
    y1.append(distance[1][0] / 10 + 0.1)
    y2.append(distance[1][1] / 10 + 0.1)
    y3.append(distance[1][2] / 10 + 0.1)

x_o, y_o = encode.encode_wave([4, 3])

degree = 300
coefficients = np.polyfit(x, y1, degree)
polynomial = np.poly1d(coefficients)
y1_fit = polynomial(x)

print(decode.decode(x, y1_fit))
print(decode.decode(x_o, y_o))

plt.plot(x, y1)
plt.plot(x, y1_fit)
plt.plot(x_o, y_o)
plt.show()

# x, y = encode.encode_wave([0x0F, 0xFF, 0xFF])
# print(decode.decode(x, y))

