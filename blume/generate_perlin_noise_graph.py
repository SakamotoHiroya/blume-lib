import generate_perlin_noise_graph as gpng
import triming as trim
import output

def generate_perlin_noise_graph(image_path):

    gpng.crop_to_non_bg(image_path)
    trim.crop_to_non_bg('line_drawing_output.jpg')
    