import math
import noise
import numpy as np
import random

def add_play(value, max_play):
    return value + random.uniform(-max_play, max_play)

def to_slopes(bytes):
    value_rad_dic = {
        0: math.tan(-math.pi / 3),
        1: math.tan(-math.pi / 6),
        2: math.tan(0),
        3: math.tan(math.pi / 6)
    }
    play = math.pi / 14

    slopes = []
    for byte in bytes:
        slopes.append(math.tan(add_play(value_rad_dic[byte & 0x03], play)))
        slopes.append(math.tan(add_play(value_rad_dic[(byte & 0x0C) >> 2], play)))
        slopes.append(math.tan(add_play(value_rad_dic[(byte & 0x30) >> 4], play)))
        slopes.append(math.tan(add_play(value_rad_dic[(byte & 0xC0) >> 6], play)))
    return slopes

def encode(bytes):
    slopes = to_slopes(bytes)

    x = np.arange(0, len(slopes) - 1, 0.1)
    return x, noise.generate_noise(x, slopes)

# matplotlib のインポート
import matplotlib.pyplot as plt

x, y = encode([0xab, 0xcd, 0xef])
plt.plot(x, y)
plt.show()
