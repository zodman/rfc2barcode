from distutils.core import setup

import py2exe

setup(windows=[{ 'script':'gui.py', 'icon_resources':[(1,"barcode.ico")]}])
