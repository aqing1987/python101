## fix pygame in mac 10.15 Catalina
- https://stackoverflow.com/questions/52718921/problems-getting-pygame-to-show-anything-but-a-blank-screen-on-macos-mojave

```
I have tested this on macOS 10.15 Catalina, Python 3.7.5, PyGame 2.0.0 (prerelease as of this writing) and PyGame 1.9.6 (stable as of this writing).

Initially, go to the GitHub page of Pygame and see which stable version is the latest. As of this writing, the latest stable version of PyGame is 1.9.6 and 2.0.0 is prerelease. If you want the latest (unstable/prelease just use master when cloning below), if however you want the latest stable, change branch accordingly.

Here are the steps:

Install some dependencies brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf. This requires homebrew.
Go to site-packages:
For virtual environment go to cd ~/.virtualenvs/myvirtualenv/lib/python3.X/site-packages where ~/.virtualenvs/myvirtualenv is the path to your virtual environment and python3.X is the version of your Python.
For system-wide installation go to /usr/local/lib/python3.X/site-packages where python3.X is the version of your Python.
Delete any previous pygame, pip uninstall pygame (if a pygame directory exists in site-packages then remove it: rm -rf pygame*)
Clone pygame from GitHub:
git clone https://github.com/pygame/pygame.git for the latest (possibly not stable version).
git clone -b v1.9.6 https://github.com/pygame/pygame.git for the latest (stable, based on what you checked above, v1.9.6 as of this writing)
Go into the pygame directory: cd pygame.
Run python setup.py -config -auto -sdl2.
Run python setup.py install (it will take a while).
Now PyGame should work as expected on macOS.
```

## free picture (without license)
http://pixabay.com
