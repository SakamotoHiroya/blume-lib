import generate_drawing_image as gdi
import triming as trim
import output

def generate_perlin_noise_graph(image_path):
    gdi.line_drawing_image(image_path)
    trim.crop_to_non_bg('line_drawing_output.jpg')
    center_x, center_y = output.find_smallest_circle_center('cropped_image.jpg')
    distances = output.get_circle_distances('cropped_image.jpg', center_x, center_y)
    distances = output.output(distances)

    return distances

distances = generate_perlin_noise_graph('image/8.png')