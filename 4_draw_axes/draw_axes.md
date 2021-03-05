# How to draw axes

[`draw_axes.py`](draw_axes.py)

## Draw axes

Here I create 3 lines in 3D coordinates system. I color z, y, z axes as red, green, blue. Then I give each line an arrow in positive domain. *The function is quite long, you might want scroll fast.*

```python
def draw_axes():
    gl.glPushMatrix()
    # red X
    gl.glColor3ub(255, 0, 0)
    gl.glBegin(gl.GL_LINES)

    # x axis
    gl.glVertex3f(-4.0, 0.0, 0.0)
    gl.glVertex3f(4.0, 0.0, 0.0)

    # arrow x
    gl.glVertex3f(4.0, 0.0, 0.0)
    gl.glVertex3f(3.0, 1.0, 0.0)
    gl.glVertex3f(4.0, 0.0, 0.0)
    gl.glVertex3f(3.0, -1.0, 0.0)

    gl.glEnd()
    gl.glFlush() # Make all previous commands executed

    # green y
    gl.glColor3ub(0, 255, 0)
    gl.glBegin(gl.GL_LINES)

    # y axis
    gl.glVertex3f(0.0, -4.0, 0.0)
    gl.glVertex3f(0.0, 4.0, 0.0)

    # arrow y
    gl.glVertex3f(0.0, 4.0, 0.0)
    gl.glVertex3f(1.0, 3.0, 0.0)
    gl.glVertex3f(0.0, 4.0, 0.0)
    gl.glVertex3f(-1.0, 3.0, 0.0)

    gl.glEnd()
    gl.glFlush() # Make all previous commands executed

    # blue z
    gl.glColor3ub(0, 0, 255)
    gl.glBegin(gl.GL_LINES)
    
    # z axis
    gl.glVertex3f(0.0, 0.0, -4.0)
    gl.glVertex3f(0.0, 0.0, 4.0)

    # arrow z
    gl.glVertex3f(0.0, 0.0, 4.0)
    gl.glVertex3f(0.0, 1.0, 3.0)
    gl.glVertex3f(0.0, 0.0, 4.0)
    gl.glVertex3f(0.0, -1.0, 3.0)

    gl.glEnd()
    gl.glFlush() # Make all previous commands executed

    gl.glPopMatrix()
```

Expected outcome: 3 axes but only x, y seen

## Setup point of view

I create an eye at 10, 10, 10 to look at 0, 0, 0 which is the origin of 3 axes. The eye is defined in `render_scene()`

```python
def render_scene():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # Clear everything in scene
    
    # Put functions to draw here
    # draw_func()    
    draw_axes()

    glut.glutSwapBuffers()

    # Define Eye ~ Camera
    Eye = {"eyeX": 10.0, "eyeY": 10.0, "eyeZ": 10.0,
            "centerX": 0.0, "centerY": 0.0, "centerZ": 0.0,
            "upX": 0.0, "upY": 1.0, "upZ": 0.0}

    glu.gluLookAt(Eye['eyeX'], Eye['eyeY'], Eye['eyeZ'],
                    Eye['centerX'], Eye['centerY'], Eye['centerZ'],
                    Eye['upX'], Eye['upY'], Eye['upZ'])
```

Expected outcome: a blank scene

## Handle changes

Because I am changing view port by moving the eye, I need to tell the program what to do. Every change is defined in `reshape_scene()`

```python
def reshape_scene(width: int, height: int):
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glViewport(0, 0, width, height) # Set viewport = window
    glu.gluPerspective(60, 1.0, 1.0, 100) # fovy, ratio, near, far
    gl.glMatrixMode(gl.GL_MODELVIEW)
```

Then I use `glut.glutReshapeFunc()` receive `reshape_scene()`

```python
if __name__ == '__main__':
    # other lines

    glut.glutReshapeFunc(reshape_func) # Pass a function to handle the change

    glut.glutMainLoop() # Keep window alive
```

Because I am switching matrix mode, I need to add `gl.glLoadIdentity()` to reset matrices in `renderScene()`

```python
def render_scene():
    # other lines

    glut.glutSwapBuffers()
    gl.glLoadIdentity()

    # other lines
```

## Put everything together

[`draw_axes.py`](draw_axes.py)

Expected outcome: 3 visible axes that are balanced in term of angles

