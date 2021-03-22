# Setup more libraries

In this tutorial, I will guide you the way to install OpenGLContext and it's dependencies properly for Python 3 on Windows 10. For Unix and GNU/Linux users, you are now on your own.

## Things that you can install with `pip`

```bash
pip install numpy==1.20.1 Pillow==8.1.2
```

As of writing, I use [`numpy==1.20.1`](https://numpy.org/doc/stable/release/1.20.0-notes.html#new-functions) and [`Pillow==8.1.2`](https://pillow.readthedocs.io/en/latest/installation.html) which only support Python from 3.7

## Things that you HAVE to install from [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

```
PyDispatcher
PyVRML97
PyVRML97-accelerate
```

Go to [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/) search for these packages. Click on the version that is suitable with your Python environment. Then run `pip install path/to/package.whl` to install one by one.

In case of `PyDispatcher` and `PyVRML97`, the version is `none-any` which means that every Python version it most likely suitable.

In my case, python 3.8, windows 64, I downloaded the file `PyVRML97_accelerate-2.3.1-cp38-cp38-win_amd64.whl` for `PyVRML97-accelerate`.

## Things you HAVE to install from ME

Download this file [OpenGLContext](OpenGLContext-2.3.0-py2.py3-none-any.whl) then run `pip install path/to/package.whl`

## Try to run [basic_geometry](https://github.com/tartley/opengl-tutorials/blob/master/pyopengl/01-basic-geometry.py)

If you can run that file, you are ready to learn more about shading, lightning with OpenGL. 

Suggest tutorials cover these topic:
- [jcteng/python-opengl-tutorial](https://github.com/jcteng/python-opengl-tutorial)
- [An Introduction to Shaders in openGL](http://yvanscher.com/2018-07-26_An-Introduction-to-Shaders-in-openGL-c19a1376eda1.html)



