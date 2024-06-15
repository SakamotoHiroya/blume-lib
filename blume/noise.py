import math

import numpy as np

def linerCompletion(x, y1, y2):
    return (y2 - y1) * x + y1;

def smootherstep(x):
  return x * x * x * (x * (x * 6 - 15) + 10);


def generate_noise(x, slopes):

    if isinstance(x, list) or type(x) == np.ndarray:
        result = []
        for i in x:
            result.append(generate_noise(i, slopes))
        return result

    left = math.floor(x);
    right = left + 1;

    print(x, left, right);

    l = slopes[left] * (x - left);
    r = slopes[right] * (x - right);
    x_p = smootherstep(x - left);
    return linerCompletion(x_p, l, r);