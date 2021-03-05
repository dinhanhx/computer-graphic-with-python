# How to draw a spinning cube

[`spinning_cube.py`](spinning_cube.py)

## Draw a cube

Here I use `gl.GL_QUADS` to draw a cube. 

> GL_QUADS
>
> Treats each group of four vertices as an independent quadrilateral. Vertices 4 ⁢ n - 3 , 4 ⁢ n - 2 , 4 ⁢ n - 1 , and 4 ⁢ n define quadrilateral n. N 4 quadrilaterals are drawn.

[Khronos OpenGL C++ Doc](https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glBegin.xml)

The center of it at 0, 0, 0. Each side has length of 0.2. It's a small cube.

```python
def draw_cube():
    gl.glPushMatrix()
    gl.glBegin(gl.GL_QUADS)

    # norm x 0.1 face red 183, 18, 52
    gl.glColor3ub(183, 18, 52)
    gl.glVertex3f(0.1, -0.1, 0.1)
    gl.glVertex3f(0.1, -0.1, -0.1)
    gl.glVertex3f(0.1, 0.1, -0.1)
    gl.glVertex3f(0.1, 0.1, 0.1)

    # norm y 0.1 face green 0, 155, 72
    gl.glColor3ub(0, 155, 72)
    gl.glVertex3f(0.1, 0.1, 0.1)
    gl.glVertex3f(0.1, 0.1, -0.1)
    gl.glVertex3f(-0.1, 0.1, -0.1)
    gl.glVertex3f(-0.1, 0.1, 0.1)

    # norm z 0.1 face blue 0, 70, 173
    gl.glColor3ub(0, 70, 173)
    gl.glVertex3f(-0.1, 0.1, 0.1)
    gl.glVertex3f(0.1, 0.1, 0.1)
    gl.glVertex3f(0.1, -0.1, 0.1)
    gl.glVertex3f(-0.1, -0.1, 0.1)

    # norm x -0.1 face white 255, 255, 255
    gl.glColor3ub(255, 255, 255)
    gl.glVertex3f(-0.1, -0.1, 0.1)
    gl.glVertex3f(-0.1, 0.1, 0.1)
    gl.glVertex3f(-0.1, 0.1, -0.1)
    gl.glVertex3f(-0.1, -0.1, -0.1)

    # norm y -0.1 face orange 255, 88, 0
    gl.glColor3ub(255, 88, 0)
    gl.glVertex3f(-0.1, -0.1, -0.1)
    gl.glVertex3f(-0.1, -0.1, 0.1)
    gl.glVertex3f(0.1, -0.1, 0.1)
    gl.glVertex3f(0.1, -0.1, -0.1)

    # norm z -0.1 face yellow 255, 213, 0
    gl.glColor3ub(255, 213, 0)
    gl.glVertex3f(0.1, -0.1, -0.1)
    gl.glVertex3f(-0.1, -0.1, -0.1)
    gl.glVertex3f(-0.1, 0.1, -0.1)
    gl.glVertex3f(0.1, 0.1, -0.1)

    gl.glEnd()
    gl.glPopMatrix()
```

Expected outcome: a very small cube at the origin

## Move the eye closer to the origin

I move this eye closer by 10 times via reducing value of `eyeX`, `eyeY`, `eyeZ`.

```python
def render_scene():
    # other lines

    Eye = {"eyeX": 1.0, "eyeY": 1.0, "eyeZ": 1.0,
            "centerX": 0.0, "centerY": 0.0, "centerZ": 0.0,
            "upX": 0.0, "upY": 1.0, "upZ": 0.0}
    
    # other lines
```

Expected outcome: a bigger cube

## Make the cube spin

I define a global variable outside of main loop to update the rotation of the cube each frame.

```python
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

R_QUAD = gl.GLfloat(0.0) # Create an object of gl_float with value 0.0
```

In c++ opengl, you just create a variable like this `GLfloat R_QUAD = 0.0;`. 

Then I globalize `R_QUAD` in `draw_cube()`. `R_QUAD.value += 0.03` rotates the cube by 0.03 radian.

**Note**:
- To manipulate gl objects, use `.value`

```python
def draw_cube():
    gl.glPushMatrix()

    global R_QUAD
    gl.glRotatef(R_QUAD, 0.1, 0.0, 0.0)
    R_QUAD.value += 0.03

    gl.glRotatef(R_QUAD, 0.0, 0.1, 0.0)
    R_QUAD.value += 0.03

    gl.glRotatef(R_QUAD, 0.0, 0.0, 0.1)
    R_QUAD.value += 0.03

    gl.glRotatef(R_QUAD, 0.0, 0.1, 0.0)
    R_QUAD.value += 0.03

    gl.glBegin(gl.GL_QUADS)

    # other lines
```

Expected outcome: a little bit broken spinning cube

## Make it perfect

Now I need to make depth buffer enable to render deeper layers.

```python
if __name__ == '__main__':
    # Other lines

    gl.glEnable(gl.GL_DEPTH_TEST)

    glut.glutMainLoop() # Keep window alive
```

## Put everything together

[`spinning_cube.py`](spinning_cube.py)

Expected outcome: a spinning cube