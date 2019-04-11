import numpy as np
from PIL import Image

argv = sys.argv[1:]
source_file = argv[0]
dest_file = argv[1]

start_color = (0, 0, 0, 255) # white
new_color = (211, 211, 211, 255) # lightgray

shape_img = Image.open(source_file).convert('RGBA')
shape_data = np.array(shape_img)

shape_data[(shape_data == start_color).all(axis = -1)] = new_color
final_image = Image.fromarray(shape_data, mode='RGBA')
final_image.save(dest_file)


