# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    sky(canvas, scene_width, scene_height)
    ground(canvas, scene_width, scene_height)

    


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def ground(canvas, scene_width, scene_height):
    
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    xaxis = 170
    bottom = 50
    height = 200
    tree(canvas, xaxis , bottom, height)

    xaxis = 250
    bottom = 70
    height = 200
    tree(canvas, xaxis , bottom, height)

    xaxis =600
    bottom = 100
    height = 400
    tree(canvas, xaxis , bottom, height)

    tree_center_x = 20
    tree_bottom = 0
    tree_height = 500
    draw_fence(canvas, tree_center_x,
            tree_bottom, tree_height)
    number = 1
    while number != 14:
        tree_center_x = tree_center_x + 60
        draw_fence(canvas, tree_center_x,
            tree_bottom, tree_height)
        number = number + 1



def sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="gray")
    draw_cloud(canvas)

def tree(canvas, xaxis, bottom, height):
    width = height /10
    trunkheight = height / 8
    leftspot = xaxis - width / 2
    trunk_right = xaxis + width / 2
    trunk_top = bottom + trunkheight

    draw_rectangle(canvas,
            leftspot, trunk_top, trunk_right, bottom,
            outline="gray", width=1, fill="tan")

    skirt_width = height / 2
    skirt_height = height - trunkheight
    skirt_left = xaxis - skirt_width / 2
    skirt_right = xaxis + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, xaxis, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_cloud(canvas):
    draw_oval(canvas, 100, 400, 200, 350,width=1, outline="white", fill="white")
    draw_oval(canvas, 120, 430, 200, 350,width=1, outline="white", fill="white")
    



def draw_fence(canvas, center_x, bottom, height):
    
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="white", width=1, fill="white")

    skirt_width = height / 4
    skirt_height = 10
    skirt_left = center_x - skirt_width / 5
    skirt_right = center_x + skirt_width / 5
    skirt_top = 80

    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="white", width=1, fill="white")



# Call the main function so that
# this program will start executing.
main()
