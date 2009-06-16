from distutils.core import setup

import py2exe
import sys
sys.argv.append("py2exe")
setup(
    #options = {'py2exe':{"compressed": 1, "optimize": 2, "ascii": 1,'bundle_files':3}},
    windows=[{
        'script':'gui.py', 
        'icon_resources':[(1,"barcode.ico")]
        }],
    zipfile = None,
    )
