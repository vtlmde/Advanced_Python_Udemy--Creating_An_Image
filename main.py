from canvas import canvas
from shapes import square,rectangle

# Get canvas width and height from the user: 
canvas_width = int( input( "Enter canvas width :" ) )
canvas_height = int( input( "Enter canvas height :" ) )

# make a dictionnary of color codes and prompt for color
colors = {"white": (255,255,255), "black":(0,0,0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data 
canvas1=canvas(canvas_width,canvas_height,colors[canvas_color])

while True: 
    shape_type = input("Which shape would you like to draw? Square or Rectangle ?: ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green should the rectangle have: "))
        blue = int(input("How much blue should the rectangle have: "))

        # create the rectangle 
        r1 = rectangle ( x=rec_x , y=rec_y , height = rec_height, width = rec_width , color = (red, green, blue))
        r1.draw(canvas1)

    elif shape_type.lower() == "square":
            sqr_x = int(input("Enter x of the square: "))
            sqr_y = int(input("Enter y of the square: "))
            sqr_side = int(input("Enter the side length of the square: "))
            red = int(input("How much red should the square have: "))
            green = int(input("How much green should the square have: "))
            blue = int(input("How much blue should the square have: "))
    
            # create the square 
            sqr1 = square ( x=sqr_x , y=sqr_y ,  side= sqr_side , color = (red, green, blue))
            sqr1.draw(canvas1)
    
    else: 
        print("Not an accepted value. Generating your image and exiting now.")
        canvas1.make('canvas1.png')
        break