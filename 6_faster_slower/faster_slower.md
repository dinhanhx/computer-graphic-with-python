# How to change the speed of spinning cube

[`faster_slower.py`](faster_slower.py)

## Press `esc` to exit window

```python
# This func is a parameter of glutKeyBoardFunc()
def keyboard(key: str, x_pos: int, y_pos: int):
    if ord(key) == 27: # Esc key
        glut.glutLeaveMainLoop()
```

```python
if __name__ == '__main__':
    glut.glutInit()

    # Other lines

    glut.glutKeyboardFunc(keyboard)

    # Other lines
```

Expected outcome: when press `esc`, you should not see the window.

## Press `up` and `down`

Here I define a global variable called speed factor. This will multiply with `R_QUAD` in `draw_cube()` and other keyboard handlers.

```python
R_QUAD = gl.GLfloat(0.0) # Create an object of gl_float with value 0.0
SPEED_FACTOR = 1.0
```

```python
def draw_cube():
    # Other lines

    global R_QUAD
    global SPEED_FACTOR

    gl.glRotatef(R_QUAD, 0.1, 0.0, 0.0)
    R_QUAD.value += (0.03 * SPEED_FACTOR)

    gl.glRotatef(R_QUAD, 0.0, 0.1, 0.0)
    R_QUAD.value += (0.03 * SPEED_FACTOR)

    gl.glRotatef(R_QUAD, 0.0, 0.0, 0.1)
    R_QUAD.value += (0.03 * SPEED_FACTOR)

    gl.glRotatef(R_QUAD, 0.0, 0.1, 0.0)
    R_QUAD.value += (0.03 * SPEED_FACTOR)
```
### Press and release
```python

# This func is a parameter of glutKeyBoardFunc()
def keyboard(key: str, x_pos: int, y_pos: int):
    if ord(key) == 27: # Esc key
        glut.glutLeaveMainLoop()


# This func is a parameter of glutSpecialFunc()
def press_key(key: str, x_pos: int, y_pos:int):
    global SPEED_FACTOR
    if key == glut.GLUT_KEY_UP:
        SPEED_FACTOR = 2.0 

    if key == glut.GLUT_KEY_DOWN:
        SPEED_FACTOR = 2.0 ** -1
```
### Add to handler

```python
if __name__ == '__main__':
    # Other lines

    glut.glutKeyboardFunc(keyboard)
    glut.glutSpecialFunc(press_key)
    glut.glutSpecialUpFunc(release_key)

    # Other lines
```

Expected outcome: when you press `up`, spin faster. when you press `down`, spin lower.

[`faster_slower.py`](faster_slower.py)