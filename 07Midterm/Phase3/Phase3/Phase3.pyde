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
    drawObject(0,0,1)
    drawObject(0,200,2)
