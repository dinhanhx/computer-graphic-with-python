import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu


def draw_triangle():
    gl.glColor3ub(255, 0, 0) # Set the color to red in RGB system 
    gl.glBegin(gl.GL_TRIANGLES) # Choose primitive shape
    gl.glVertex2f(0,0) 
    gl.glVertex2f(0,1)
    gl.glVertex2f(1,0)
    gl.glEnd()


def render_scene():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # Clear everything in scene
    
    # Put functions to draw here
    # draw_func()    
    draw_triangle()

    glut.glutSwapBuffers()


if __name__ == '__main__':
    glut.glutInit()

    glut.glutInitDisplayMode(glut.GLUT_DEPTH | glut.GLUT_DOUBLE | glut.GLUT_RGBA) # Set color mode
    glut.glutInitWindowSize(640, 640) # Set window width, height
    glut.glutInitWindowPosition(0, 0) # Set window position
    wind = glut.glutCreateWindow("Draw a triangle") # Set window name

    glut.glutDisplayFunc(render_scene) # Pass a function to draw
    glut.glutIdleFunc(render_scene) # Keep it alive

    glut.glutMainLoop() # Keep window alive