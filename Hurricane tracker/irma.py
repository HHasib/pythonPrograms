import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    data = open('irma.csv', 'r')
    for line in data:

        line = line.split(',')

        if line[0] == 'Date':
            continue
        wind_speed = int(line[4])
        lat = float(line[2])
        long = float(line[3])
        category = get_cat(wind_speed)

        pen_width = [1, 3, 6, 9, 12, 15]
        pen_color = ['white', 'blue', 'green', 'yellow', 'orange', 'red']

        t.goto(long,lat)
        t.pendown()
        t.pencolor(pen_color[category])
        t.pensize(pen_width[category])

        if category == 0:
            continue
        t.write(category, align = "center", font = ("Arial", 12, "bold"))

    turtle.done()

def get_cat(ws):
    if ws >= 157:
        cat = 5
    elif ws < 157 and ws >= 130:
        cat = 4
    elif ws < 130 and ws >= 111:
        cat = 3
    elif ws < 111 and ws >= 96:
        cat = 2
    elif ws < 96 and ws >= 74:
        cat = 1
    else:
        cat = 0
    return cat

if __name__ == "__main__":
    irma()
