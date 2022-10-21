from cmu_graphics import *

## Flappy Snaouser

# App
app.stepsPerSecond = 50
app.background = 'skyBlue'

##Variabler
dosa_circle = Circle(200, 200, 30, fill='white', border='black', borderWidth=1)
stock1_rect = Rect(300, 300, 50, 100)
stock2_rect = Rect(240, 0, 50, 100)
stock3_rect = Rect(100, 260, 50, 140)
stock4_rect = Rect(40, 0, 50, 100)

# Dosa
dosa = Group(
    dosa_circle,
    Label('VELO', 200, 200, rotateAngle=-90, fill='deepSkyBlue', size=15),
    Rect(194.8, 197.5, 9, 1, fill='red'),
    Label('SLIM', 216, 196, size=5),
    Circle(211.5, 202, 1, fill='red'),
    Circle(215, 202, 1, fill='red'),
    Circle(218.5, 202, 1, fill='red'),
    Circle(222, 202, 1, fill='lightGray'),
    Label('ICE', 185, 196, size=5, fill='deepSkyBlue'),
    Label('COOL', 185, 202, size=5, fill='deepSkyBlue')
)


def onMousePress(mouseX, mouseY):
    dosa.centerY -= 40


# Stock
stock1 = Group(
    stock1_rect,
    Oval(325, 300, 50, 10, border='darkGray'),
    Rect(316, 298, 18, 4, fill='darkGreen'),
    Label('Lundgrens', 325, 300, size=3),
    Rect(300, 310, 50, 10, fill='darkGreen'),
    Oval(325, 310, 50, 2, fill='darkGreen'),
    Oval(325, 320, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 325, 315, size=5),
    Rect(300, 330, 50, 10, fill='darkGreen'),
    Oval(325, 330, 50, 2, fill='darkGreen'),
    Oval(325, 340, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 325, 335, size=5),
    Rect(300, 350, 50, 10, fill='darkGreen'),
    Oval(325, 350, 50, 2, fill='darkGreen'),
    Oval(325, 360, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 325, 355, size=5),
    Rect(300, 370, 50, 10, fill='darkGreen'),
    Oval(325, 370, 50, 2, fill='darkGreen'),
    Oval(325, 380, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 325, 375, size=5),
    Rect(300, 390, 50, 10, fill='darkGreen'),
    Oval(325, 390, 50, 2, fill='darkGreen'),
    Oval(325, 400, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 325, 395, size=5),
)

stock2 = Group(
    stock2_rect,
    Oval(265, 100, 50, 10, border='darkGray'),
    Rect(256, 98, 18, 4, fill='royalBlue'),
    Label('Lundgrens', 265, 100, size=3),
    Rect(240, 80, 50, 10, fill='royalBlue'),
    Oval(265, 80, 50, 2, fill='royalBlue'),
    Oval(265, 90, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 265, 85, size=5),
    Rect(240, 60, 50, 10, fill='royalBlue'),
    Oval(265, 60, 50, 2, fill='royalBlue'),
    Oval(265, 70, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 265, 65, size=5),
    Rect(240, 40, 50, 10, fill='royalBlue'),
    Oval(265, 40, 50, 2, fill='royalBlue'),
    Oval(265, 50, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 265, 45, size=5),
    Rect(240, 20, 50, 10, fill='royalBlue'),
    Oval(265, 20, 50, 2, fill='royalBlue'),
    Oval(265, 30, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 265, 25, size=5),
    Rect(240, 0, 50, 10, fill='royalBlue'),
    Oval(265, 0, 50, 2, fill='royalBlue'),
    Oval(265, 10, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 265, 5, size=5)
)

stock3 = Group(
    stock3_rect,
    Oval(125, 260, 50, 10, border='darkGray'),
    Rect(116, 258, 18, 4, fill='darkGreen'),
    Label('Lundgrens', 125, 260, size=3),
    Rect(100, 270, 50, 10, fill='darkGreen'),
    Oval(125, 270, 50, 2, fill='darkGreen'),
    Oval(125, 280, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 125, 275, size=5),
    Rect(100, 290, 50, 10, fill='darkGreen'),
    Oval(125, 290, 50, 2, fill='darkGreen'),
    Oval(125, 300, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 125, 295, size=5),
    Rect(100, 310, 50, 10, fill='darkGreen'),
    Oval(125, 310, 50, 2, fill='darkGreen'),
    Oval(125, 320, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 125, 315, size=5),
    Rect(100, 330, 50, 10, fill='darkGreen'),
    Oval(125, 330, 50, 2, fill='darkGreen'),
    Oval(125, 340, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 125, 335, size=5),
    Rect(100, 350, 50, 10, fill='darkGreen'),
    Oval(125, 350, 50, 2, fill='darkGreen'),
    Oval(125, 360, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 125, 355, size=5),
    Rect(100, 370, 50, 10, fill='darkGreen'),
    Oval(125, 370, 50, 2, fill='darkGreen'),
    Oval(125, 380, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 125, 375, size=5),
    Rect(100, 390, 50, 10, fill='darkGreen'),
    Oval(125, 390, 50, 2, fill='darkGreen'),
    Oval(125, 400, 50, 2, fill='darkGreen'),
    Label('LUNDGRENS', 125, 395, size=5),
)

stock4 = Group(
    stock4_rect,
    Oval(65, 100, 50, 10, border='darkGray'),
    Rect(56, 98, 18, 4, fill='royalBlue'),
    Label('Lundgrens', 65, 100, size=3),
    Rect(40, 80, 50, 10, fill='royalBlue'),
    Oval(65, 80, 50, 2, fill='royalBlue'),
    Oval(65, 90, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 65, 85, size=5),
    Rect(40, 60, 50, 10, fill='royalBlue'),
    Oval(65, 60, 50, 2, fill='royalBlue'),
    Oval(65, 70, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 65, 65, size=5),
    Rect(40, 40, 50, 10, fill='royalBlue'),
    Oval(65, 40, 50, 2, fill='royalBlue'),
    Oval(65, 50, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 65, 45, size=5),
    Rect(40, 20, 50, 10, fill='royalBlue'),
    Oval(65, 20, 50, 2, fill='royalBlue'),
    Oval(65, 30, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 65, 25, size=5),
    Rect(40, 0, 50, 10, fill='royalBlue'),
    Oval(65, 0, 50, 2, fill='royalBlue'),
    Oval(65, 10, 50, 2, fill='royalBlue'),
    Label('LUNDGRENS', 65, 5, size=5)
)

# Scoreboard
Rect(180, 30, 40, 20)
counter = Label(0, 200, 40, size=15, fill='white')


# dosa och stock functions

def onStep():
    if dosa.centerX == stock1.centerX and dosa.centerY < stock1.top:
        counter.value += 1
    elif dosa.centerX == stock2.centerX and dosa.centerY > stock2.top:
        counter.value += 1
    elif dosa.centerX == stock3.centerX and dosa.centerY < stock3.top:
        counter.value += 1
    elif dosa.centerX == stock4.centerX and dosa.centerY > stock4.top:
        counter.value += 1

    dosa.centerY += 1
    stock1.centerX -= 1
    stock2.centerX -= 1
    stock3.centerX -= 1
    stock4.centerX -= 1

    if stock1.right == 1:
        stock1.left = 399

    if stock2.right == 1:
        stock2.left = 399

    if stock3.right == 1:
        stock3.left = 399

    if stock4.right == 1:
        stock4.left = 399

    if (dosa.hits(stock1_rect.left, stock1_rect.top) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock1_rect.right, stock1_rect.top) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock1_rect.left, stock1_rect.centerY) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock1_rect.right, stock1_rect.centerY) == True):
        app.stepsPerSecond = 0

    if (dosa.hits(stock2_rect.left, stock2_rect.bottom) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock2_rect.right, stock2_rect.bottom) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock2_rect.left, stock2_rect.centerY) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock2_rect.right, stock2_rect.centerY) == True):
        app.stepsPerSecond = 0

    if (dosa.hits(stock3_rect.left, stock3_rect.top) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock3_rect.right, stock3_rect.top) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock3_rect.left, stock3_rect.centerY) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock3_rect.right, stock3_rect.centerY) == True):
        app.stepsPerSecond = 0

    if (dosa.hits(stock4_rect.left, stock4_rect.bottom) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock4_rect.right, stock4_rect.bottom) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock4_rect.left, stock4_rect.centerY) == True):
        app.stepsPerSecond = 0
    elif (dosa.hits(stock4_rect.right, stock4_rect.centerY) == True):
        app.stepsPerSecond = 0

    if dosa.bottom == 400:
        app.stepsPerSecond = 0
    elif dosa.top == 0:
        app.stepsPerSecond = 0

    if app.stepsPerSecond == 0:
        Rect(75, 150, 250, 100, fill='darkGreen', border='black')
        Label("Game Over", 200, 190, size=25)
        Label("Highscore: ", 200, 220)
        Label(counter.value, 232, 220)
        dosa.visible = False


cmu_graphics.run()
