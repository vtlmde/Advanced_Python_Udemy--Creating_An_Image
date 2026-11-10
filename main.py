import numpy as np
from PIL import Image

class square:

    """
    a square color patch on the canva
    """
    
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw (self, canvas):
        pass

class rectangle: 

    """
    a rectangular color patch on the canva
    """

    def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
    
    def draw (self, canvas):
        pass

class canvas:

    """
        a white canva on which color patches will be applied to create an image.
    """
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    
    def make (imagepath):
         pass