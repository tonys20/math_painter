import numpy as np
from PIL import Image

color_lookup = {
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Blue': (0, 0, 255),
    'White': (255, 255, 255),
    'Black': (0, 0, 0),
    'Yellow': (255, 255, 0),
    'Cyan': (0, 255, 255),
    'Magenta': (255, 0, 255),
    'Silver': (192, 192, 192),
    'Gray': (128, 128, 128),
    'Maroon': (128, 0, 0),
    'Olive': (128, 128, 0),
    'Purple': (128, 0, 128),
    'Teal': (0, 128, 128),
    'Navy': (0, 0, 128),
}


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self):
        canvas_array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        if self.color not in color_lookup.keys():
            raise KeyError('Color not supported')

        canvas_array[:, :] = color_lookup[self.color]
        return canvas_array


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas_array):
        canvas_array[self.x: self.x + self.width, self.y: self.y + self.height] = color_lookup[self.color]


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas_array):
        canvas_array[self.x: self.x + self.side, self.y: self.y + self.side] = color_lookup[self.color]


def visualize(canvas_array):
    image = Image.fromarray(canvas_array, 'RGB')
    image.save('canvas.png')


canvas_w = int(input('Please enter a canvas width'))
canvas_h = int(input('Please enter a canvas height'))
canvas_c = input('Enter a Canvas color: e.g. Black')
canvas = Canvas(canvas_w, canvas_h, canvas_c).make()

shape_selector = input('What would you like to draw? square, rectangle, quit')
while shape_selector != 'quit':
    if shape_selector not in ('rectangle', 'square'):
        shape_selector = input('please select from one of square, rectangle, quit')
    elif shape_selector == 'rectangle':
        rect_x = int(input('Enter the starting x coordinate of the rectangle'))
        rect_y = int(input('Enter the starting y coordinate of the rectangle'))
        rect_w = int(input('Enter the width of the rectangle'))
        rect_h = int(input('Enter the height of the rectangle'))
        rect_c = input('Enter the color of the rectangle')
        rect = Rectangle(rect_x, rect_y, rect_w, rect_h, rect_c)
        rect.draw(canvas)
    else:
        sq_x = int(input('Enter the starting x coordinate of the Square'))
        sq_y = int(input('Enter the starting y coordinate of the Square'))
        sq_s = int(input('Enter the side of the Square'))
        sq_color = input('Enter the color of the Square')
        sq = Square(sq_x, sq_y, sq_s, sq_color)
        sq.draw(canvas)
        shape_selector = input('What would you like to draw? square, rectangle, quit')

visualize(canvas_array=canvas)


