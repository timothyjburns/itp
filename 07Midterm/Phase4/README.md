# Burns Midterm

## Phase 4

- Copied the "setup" and "drawObject" functions into the new Phase4 Processing sketch

- Created a nested "for" loop for the "draw" function as suggested, with a range of 0-600 (as my canvas is 600x600)

- Tested with "drawObject(x, y, 1)"

*PROBLEM* the code is currently demanding that Processing draws the object at EVERY pixel, without considering the gap.

*SOLUTION* For the sake of testing, I changed the "range" to "range(0, width, 150)", where 150 is the width of the object, and did the same for the y axis. This produces a 4x4 grid, as the image is 150x150 in a 600x600 canvas.

- I wanted to create a variable for the grid size, which will affect the step size of the "range" function & the scale size of the "drawObject" function. I called it "square_grid". The number of images on the canvas should be equal to the square of "square_grid"

- The step size will equal 600 (the height & width) divided by square_grid, or:

```
step = width / square_grid
```

- Replaced the step size in "range" with "step"

- Created a variable "s" for scale size, where:

```
s = 4 / square_grid
```
as the object is 1/4 of the whole canvas when the scale is 1.

*PROBLEM* For the scale function to work, "s" has to be a float.

*SOLUTION* Changed the "s" to:

```
s = float(4) / square_grid
```

- This all works, but for obvious reasons it only produces the desired effect when square_grid is a factor of 600, the height & width of the canvas.
