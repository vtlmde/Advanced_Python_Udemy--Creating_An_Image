from PIL import Image
import numpy as np

class canvas:

    """
        a white canva on which color patches will be applied to create an image.
    """
    
    def __init__(self, width, height,color):
        self.width = width
        self.height = height
        self.color = color 
        # create an all white array
        self.array = np.zeros((width,height,3), dtype=np.uint8)
        self.array[:] = self.color
    
    def make (self, path):
        img = Image.fromarray(self.array,'RGB')
        img.save(path)