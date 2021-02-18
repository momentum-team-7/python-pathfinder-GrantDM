#primary for python code here
from PIL import Image, ImageDraw

def small_map_elevation():
    with open('elevation_small.txt', "r") as map_small_file:
        map_data = []
        for data in map_small_file:
            # small_map = map_small_file.read()
            map_data.append(data.split())
            
        im = Image.new('RGB', (500,300), ('red'))
        draw = ImageDraw.Draw(im)
        # draw.point(map_data, 'red')
        im.show()

        len(map_data[0])
        

small_map_elevation()