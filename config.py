fps = 120
caption = "PlottingPG"

HEIGHT = 600
WIDTH = 800

SC_F = HEIGHT / (WIDTH*100)

# grid space

# y-line
y_a = [WIDTH * SC_F, HEIGHT]
y_b = [WIDTH * SC_F, 0]

# x-line
x_a = [WIDTH, HEIGHT-(HEIGHT//2)]
x_b = [0, HEIGHT-(HEIGHT//2)]

# dividing line
d_a = [WIDTH//2, WIDTH]
d_b = [WIDTH//2, 0]

# circle mesh
circle_centre = (WIDTH-(WIDTH//4), (HEIGHT//2))

yc_a = [WIDTH-(WIDTH//4), 0]
yc_b = [WIDTH-(WIDTH//4), WIDTH]

# circle settings
ANGLE = 0
RADIUS = (WIDTH//4)*HEIGHT//WIDTH


# basic colors
white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
red_dark = (150, 0, 0)

green_dark = (0, 75, 0)
green = (0, 255, 0)

blue_dark = (0, 0, 75)
blue = (0, 0, 255)

gray = (150, 150, 150)
gray_w = (200, 200, 200)
gray_b = (100, 100, 100)


