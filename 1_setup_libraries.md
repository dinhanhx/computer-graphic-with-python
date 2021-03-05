# Setup libraris

## PyOpenGL

### For Unix/Linux user

As far as I am concerned, it's very simple to install with `pip`.

`pip install PyOpenGL PyOpenGL_accelerate`

### For Windows user

According to [PyOpenGL Documentation](http://pyopengl.sourceforge.net/documentation/installation.html), installing via PIP **should** work

`pip install PyOpenGL PyOpenGL_accelerate`

**It doesn't work irl. If you have installed via pip, please uninstall them.**

Now please go to this site for Unofficial Windows Binaries for Python Extension Packages to get `.whl` files to install PyOpenGL.

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl

Now check your Python version and Windows bit version. Then download PyOpenGL_accelerate and PyOpenGL files corresponding to your enviroment.

In my case, Python 3.8 and Windows 64 bit. I had to download these files then install:
```
PyOpenGL_accelerate‑3.1.5‑cp38‑cp38‑win_amd64.whl
PyOpenGL‑3.1.5‑cp38‑cp38‑win_amd64.whl
```

Note:
- `amd64` is for Windows 64 bit
- `cp38-cp38` is for Python 3.8

Then you just need `pip install` whl files.

`pip install path/to/filename.whl`

## Other alternative libraries

In this section, I just introduce to you that there are libraries with better peformance and high productivity. I will not conver the usage of them in further tutorials.

### [ModernGL](https://github.com/moderngl/moderngl)

Alternatively, you can choose to use ModernGL which is recommended by a lot of people on Stackoverflow.

> In contrast, ModernGL is easy to learn and use, moreover it is capable of rendering with high performance and quality, with less code written.

~ ModernGL ~

Installation is very simple

```
pip install moderngl moderngl-window
```

Documentation:
- [moderngl](https://moderngl.readthedocs.io/en/latest/)
- [moderngl-window](https://moderngl-window.readthedocs.io/en/latest/) for managing window, mouse, keyboard

### [Pyglet](https://github.com/pyglet/pyglet)

Alternatively, you can use [`pyglet.gl`](https://pyglet.readthedocs.io/en/latest/programming_guide/gl.html).

Installation is very simple

```
pip install pyglet
```

Documentation:
- [pyglet](https://pyglet.readthedocs.io/en/latest/index.html#)
 






