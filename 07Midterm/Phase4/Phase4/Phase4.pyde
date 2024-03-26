def setup():
    size(600, 600)
    noStroke()
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(241, 95, 39)
    ellipse(75, 75, 150, 120)
    fill(0)
    ellipse(75, 75, 140, 100)
    fill(253, 219, 34)
    rect(60, 75, 30, 60)
    triangle(60, 75, 90, 60, 90, 75)
    ellipse(75, 22.5, 35, 35)
    fill(255)
    ellipse(75, 22.5, 15, 15)
    pop()

def draw():
    square_grid = 3
    step = (width / square_grid)
    s = float(4) / square_grid
    for x in range(0, width, step):
        for y in range(0, height, step):
            drawObject(x, y, s)
