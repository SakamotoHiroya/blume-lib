import math
import noise
import numpy as np
import random
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

def add_play(value, max_play):
    return value + random.uniform(-max_play, max_play)

def valueToSlope(value):
    if value == 0:
        return math.tan(math.pi * 3 / 8)
    elif value == 1:
        return math.tan(math.pi / 8)
    elif value == 2:
        return math.tan(-math.pi / 8)
    elif value == 3:
        return math.tan(-math.pi * 3 / 8)

def to_slopes(bytes):

    slopes = []
    for byte in bytes:
        slopes.append(valueToSlope((byte & 0xC0) >> 6))
        slopes.append(valueToSlope((byte & 0x30) >> 4))
        slopes.append(valueToSlope((byte & 0x0C) >> 2))
        slopes.append(valueToSlope(byte & 0x03))
    return slopes

def encode_wave(bytes):
    slopes = to_slopes(bytes)
    slopes[0] = 2

    x = np.arange(0, len(slopes) - 1, 0.01)
    return x, noise.generate_noise(x, slopes)

def encode_circle(base_radius, noise_strength, bytes):
    slopes = to_slopes(bytes)
    slopes[0] = 2

    x_max = len(slopes) - 1
    x = np.arange(0, x_max, 0.01)
    y = noise.generate_noise(x, slopes)

    theta = x * 2 * math.pi / x_max
    r = list(map(lambda x: x*noise_strength+base_radius, y))

    return theta, r

def draw_flower_circle(draw, center, base_radius, noise_strength, bytes):
    theta, r = encode_circle(base_radius, noise_strength, bytes)
    points = [];

    for theta_value, r_value in zip(theta, r):
        x = math.cos(theta_value) * r_value
        y = math.sin(theta_value) * r_value
        points.append((x + center[0], y + center[1]))

    draw.polygon(points, outline=(255, 255, 255), fill=None)

def encode_flower_image(width, height, base_radius, noise_strength, bytes1, bytes2, bytes3):

    background_color = (0, 0, 0)
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    center = (width / 2, height / 2)

    draw_flower_circle(draw, center, base_radius, noise_strength, bytes1)
    draw_flower_circle(draw, center, base_radius * 0.6, noise_strength * 0.7, bytes2)
    draw_flower_circle(draw, center, base_radius * 0.2, noise_strength * 0.5, bytes3)

    draw.ellipse((center[0] - 5, center[1] - 5, center[0] + 5, center[1] + 5), outline=(255, 255, 255), fill=None, width=1)

    return image

