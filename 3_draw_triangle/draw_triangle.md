# How to draw a triangle

[`draw_triangle.py`](draw_triangle.py)

## Import

The way **I think** you should import libraries. Importing like this can reduce the time of autocomplete in term of searching and the time of compiler in term of getting functions. 

```python
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

# when call function, you need <namespace>.<function>
```

But if you are familiar with c++ code, you can import like this

```python
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# when call function, you just need name of function
```

Read more:
- [Python Import](https://stackabuse.com/relative-vs-absolute-imports-in-python/)

## Basic structure of a PyOpenGL program

```python
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def render_scene():
    gl.glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear everything in scene

    # Put functions to draw here
    # draw_func()

    glut.glutSwapBuffers()


if __name__ == '__main__':
    glut.glutInit()

    glut.glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA) # Set color mode
    glut.glutInitWindowSize(640, 640) # Set window width, height
    glut.glutInitWindowPosition(0, 0) # Set window position
    wind = glut.glutCreateWindow("Draw a triangle") # Set window name

    glut.glutDisplayFunc(render_scene) # Pass a function to draw
    glut.glutIdleFunc(render_scene) # Keep it alive

    glut.glutMainLoop() # Keep window alive
```

Expected output: a blank window

## Draw a triangle

```python
def draw_triangle():
    gl.glColor3ub(255, 0, 0) # Set the color to red in RGB system 
    gl.glBegin(gl.GL_TRIANGLES) # Choose primitive shape
    gl.glVertex2f(0,0) 
    gl.glVertex2f(0,1)
    gl.glVertex2f(1,0)
    gl.glEnd()
```

```python
def render_scene():
    gl.glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear everything in scene

    # Put functions to draw here
    # draw_func()
    draw_triangle()

    glut.glutSwapBuffers()
```

**Note**:
- [OpenGL use right-handed coordinate system](https://learnopengl.com/Getting-started/Coordinate-Systems)

## Put everything together

[`draw_triangle.py`](draw_triangle.py)

Expected outcome: a red triangle