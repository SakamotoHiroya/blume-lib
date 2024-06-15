import math
import random
import sympy
import numpy as np
import noise

def compute_data_length(x_list):
    return math.floor(max(x_list)) + 1

def filter_coordinates(x_list, y_list, x_val):
    filtered_x_list = []
    filtered_y_list = []
    for i in range(len(x_list)):
        if math.floor(x_list[i]) == x_val:
            filtered_x_list.append(x_list[i])
            filtered_y_list.append(y_list[i])
    return filtered_x_list, filtered_y_list

def pickup_random_coordinate(x_list, y_list):
    #index = 0
    #while not(0.01 < x_list[index] < 0.99):
        
    index = random.choice(range(len(x_list)))
    return x_list[index], y_list[index]

def compute_slope(x, y,left_slope):
    return (left_slope * x * (1 - noise.smootherstep(x)) - y) / (noise.smootherstep(x) * (1 - x))

def slope_to_data(slope):
    if isinstance(slope, list) or type(slope) == np.ndarray:
        result = []
        for i in slope:
            result.append(slope_to_data(i))
        return result

    if slope > 1:
        return 0
    elif slope > 0:
        return 1
    elif slope > -1:
        return 2
    else:
        return 3

def decode(x_list, y_list):

    slopes = [2]

    data_length = compute_data_length(x_list)
    for i in range(data_length):
        filtered_x_list, filtered_y_list = filter_coordinates(x_list, y_list, i);
        if(len(filtered_x_list) < 2):
            raise ValueError("error!")
        else:
            x, y = pickup_random_coordinate(filtered_x_list, filtered_y_list)

            right_slope = compute_slope(x - math.floor(x), y, slopes[i])

            slopes.append(right_slope)

    data_2bit = slope_to_data(slopes)

    data = []
    for i in range(0, len(data_2bit), 4):
        data.append((data_2bit[i] << 6) | (data_2bit[i+1] << 4) | (data_2bit[i+2] << 2) | (data_2bit[i+3]))

    return data
