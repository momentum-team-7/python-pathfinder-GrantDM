#primary for python code here
from PIL import Image, ImageDraw, ImageColor

# SMALL_MOUNTAIN = 'elevation_small.txt'
# LARGE_MOUNTAIN = 'elevation_large.txt'
# test_file = 'testingV2.txt'

# def open_file(file):
#     with open(file, 'r') as info:
#         all_txt_data = info.readlines()
#         return all_txt_data

# def get_dimensions(txt_data):
#         all_txt_data = txt_data
#         return len(all_txt_data), len(all_txt_data[0].split())

# def get_min_elevation(txt_data):
#     return min(min(txt_data).split())

# def get_max_elevation(txt_data):
#     return max(max(txt_data).split())

# def get_color_value(elevation, minimum, maximum):
#     result = ((int(elevation) - int(minimum)) /
#               (int(maximum) - int(minimum))) * 255

#     return (int(result), int(result), int(result))

# def create_picture():
#     txt_data = open_file(SMALL_MOUNTAIN)
#     dimensions = get_dimensions(txt_data)
#     im = Image.new("RGBA", (dimensions))
#     minimum = get_min_elevation(txt_data)
#     maximum = get_max_elevation(txt_data)

#     for x in range(dimensions[0]):
#         for y in range(dimensions[1]):
#             im.putpixel((x, y), get_color_value(
#                 txt_data[x].split()[y], minimum, maximum))
#     im.save('testImg.png')
# create_picture()

#! end of rewrite

def christopher_walking():
    # with open('testingV2.txt', 'r') as testing_file:
    #     mapped_data = []
    #     test_data = testing_file.readlines()
    #     print(test_data)

    with open('elevation_small.txt') as map_test:
        grid_data = [line.split() for line in map_test.readlines()]

    print(f'The color matrix is {len(grid_data)} lines tall and {len(grid_data[0])} lines wide')

    print(min(min(grid_data)))
    print(max(max(grid_data)))
    min_elevation = min(min(grid_data))
    max_elevation = max(max(grid_data))
    
    # get_color_value = ((int(elevation) - int(min_elevation)) / (int(max_elevation) - int(min_elevation))) * 255

    img = Image.new('RGB', (len(grid_data[0]), len(grid_data)))

    for y in range(len(grid_data)):
        for x in range(len(grid_data[0])):
            elevation = grid_data[y][x]
            get_color_value = ((int(elevation) - int(min_elevation)) / (int(max_elevation) - int(min_elevation))) * 255
            img.putpixel((x, y), (int(get_color_value), int(get_color_value), int(get_color_value)))
        img.save('smallimg.png')

        # for line in testing_file.readlines():
        #     mapped_data.append(line.split())
        
        # min_elevation = min(map(min, mapped_data))
        # min_elevation = int(min_elevation)
        # print(min_elevation)  

        # max_elevation = max(map(max, mapped_data))
        # max_elevation = int(max_elevation)
        # print(max_elevation)
        

    # print('len checks info', len(mapped_data),len(mapped_data[0].split()))

    # im = Image.new("RGBA", (600, 600))
    # minimum = min_elevation
    # maximum = max_elevation


    # for x in range(mapped_data[0]):
    #     for y in range(len(mapped_data)):
    #         im.putpixel((x, y), get_color_value(
    #             mapped_data[x].split()[y], minimum, maximum))
    # im.save('testImg.png')

        # list_comprehension = [column[0] for column in mapped_data]
        # start_index = list_comprehension.index(min(list_comprehension))
        # print(min(list_comprehension))
        # print(start_index)

        # for y in range(len(mapped_data)):
            
        #     list_comprehension = [column[y] for column in mapped_data]

        #     # find closest value in list comprehension columns
        #     # index of the closest value
        #     # store 2 variables to a list

        #     # min(list_comprehension)
        #     diff_index = list_comprehension.index()
        #     list_comprehension.index(list_comprehension)
                

# list_comprehension value - new value = difference
# lowest difference of values is where we step too
# make negatives into whole numbers for comparison


    # #                 y  x
    # print(mapped_data[0][2])
    # print(mapped_data)



# create_picture()
christopher_walking()

# def small_map_elevation():
#     with open('test.txt', "r") as map_small_file:
#         map_data = []
#         # small_map = map_small_file.read().strip()
#         # map_data = map_small_file.readlines()
#         for line in map_small_file.readlines():
#             map_data.append(line.split())

#         min_elevation = min(map(min, map_data))
#         min_elevation = int(min_elevation)
#         print(min_elevation)  

#         max_elevation = max(map(max, map_data))
#         max_elevation = int(max_elevation)
#         print(max_elevation)
    
#         print('testing readlines', map_data)
#         # im = Image.new('RGBA', (100,100))
#         # im.getpixel((0,0))
#         # for x in range(map_data[0]):
#         #     for y in range(x):
#         #         print(x,y)
#         #         im.putpixel((x,y), (200, 200, 200))
#         # im.show()
        

#         # im = Image.new('RGBA', (100, 100))
#         # im.getpixel((0,0))
#         # for x in range(100):
#         #     for y in range(50):
#                 # im.putpixel((x,y), (210, 210, 210))
        
#         # for x in range(100):
#         #     for y in range(50,100):
#         #         im.putpixel((x,y), ImageColor.getcolor('darkgray', 'RGBA'))
#         # im.getpixel((0,0))
#         # im.getpixel((0,50))
#         # im.save('putpixel.png')

#         im = Image.new('RBGA', len(map_data), len(map_data[0])

        # for x in map_data[0]:
        #     for y in x[1]:
        #         im.putpixel((x,y), get_color_value(map_data[x][y], min_elevation, max_elevation))
        # im.save('testvalue.png')
        

#         #some kinda setup to target the elevation    
        
#         # elevation = 4000
#         # color_value = int((elevation - min_elevation) / (max_elevation - min_elevation)) * 255
        
#         # im = Image.new('RGB', (600,600), get_color_value())
#         # draw = ImageDraw.Draw(im)
#         # im.show()
        
#         # for data in map_data:
#         #     elevation = len(map_data), len(map_data[data].split())
        
#         # print(elevation)
#         # print('2nd list print', map_data[variable][variable])

        

#         # small_map_copy = small_map.copy()
#         # small_map_copy.sort()
#         # ele_diff = (int(small_map_copy[-1]) - int(small_map_copy[0]))
        # min_elevation = int(small_map_copy[0])
#         # max_eleveation = int(small_map_copy[-1])
#         # print('Largest element', small_map_copy[-1])
#         # print('Smallest element', small_map_copy[0])
#         # print('difference in elements', ele_diff)
#         # print(type(small_map[0]))
#         # x = range(ele_diff)
#         # for i in x:
#         #     print(i)
#         # for data in small_map:
#         # for data in small_map:
#         #     elevation = int(small_map[data])

#         # for data in map_data:
#         #     # map_data = map_data.replace("\n", " ")
#         #     # test[data] = map_data[data]

#         # color_value = ((elevation - min_elevation) / (max_eleveation - min_elevation)) * 255

#         # print('first element elevation', elevation[0])

#             # difference is 2509
#         #? example percent, 5648 - 3139 = 2509
#         #? 4000 - 3139 = 861
#         #?  861 / 2509 = 0.343 * 100 = 34.3%
#         #?  255 * 0.343 = 87.4
            
#         # draw.point(map_data, 'red')
#         # print('Largest element inside data', max(map_small_file)
#         # len(map_data[0])
#     # print(small_map)

# #? largest number is 5648, smallest number is 3139

# def get_color_value(elevation, min, max):
#     color_value = ((int(elevation) - min) / (max - min)) * 255

#     return (int(color_value), int(color_value), int(color_value))




# small_map_elevation()