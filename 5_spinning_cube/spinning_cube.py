import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

R_QUAD = gl.GLfloat(0.0) # Create an object of gl_float with value 0.0

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


def render_scene():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # Clear everything in scene
    
    # Put functions to draw here
    # draw_func()    
    draw_axes()
    draw_cube()

    glut.glutSwapBuffers()
    gl.glLoadIdentity()

    # Define Eye ~ Camera
    Eye = {"eyeX": 1.0, "eyeY": 1.0, "eyeZ": 1.0,
            "centerX": 0.0, "centerY": 0.0, "centerZ": 0.0,
            "upX": 0.0, "upY": 1.0, "upZ": 0.0}

    glu.gluLookAt(Eye['eyeX'], Eye['eyeY'], Eye['eyeZ'],
                    Eye['centerX'], Eye['centerY'], Eye['centerZ'],
                    Eye['upX'], Eye['upY'], Eye['upZ'])


def reshape_scene(width: int, height: int):
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glViewport(0, 0, width, height) # Set viewport = window
    glu.gluPerspective(60, 1.0, 1.0, 100) # fovy, ratio, near, far
    gl.glMatrixMode(gl.GL_MODELVIEW)


if __name__ == '__main__':
    glut.glutInit()

    glut.glutInitDisplayMode(glut.GLUT_DEPTH | glut.GLUT_DOUBLE | glut.GLUT_RGBA) # Set color mode
    glut.glutInitWindowSize(640, 640) # Set window width, height
    glut.glutInitWindowPosition(0, 0) # Set window position
    wind = glut.glutCreateWindow("Draw axes") # Set window name

    glut.glutDisplayFunc(render_scene) # Pass a function to draw
    glut.glutIdleFunc(render_scene) # Keep it alive

    glut.glutReshapeFunc(reshape_scene) # Pass a function to handle the change

    gl.glEnable(gl.GL_DEPTH_TEST)

    glut.glutMainLoop() # Keep window alive