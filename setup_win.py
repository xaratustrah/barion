#!/usr/bin/env python
"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah

py2exe setup.py written with the help of
http://stackoverflow.com/questions/31680439/exe-built-with-cx-freeze-pyqt5-python3-cant-import-extensionloader-pyqt5-qtwi
and @carlkl
"""

from version import __version__
from distutils.core import setup
import os, sys
import py2exe
from glob import glob
import PyQt5

NAME="barion"
data_files = []
qt_platform_plugins = [("platforms", glob(PyQt5.__path__[0] + r'\plugins\platforms\*.*'))]
data_files.extend(qt_platform_plugins)

sys.argv.append('py2exe')

setup(
    name=NAME,
    version=__version__,
    url='https://github.com/xaratustrah/barion',
    license='GPLv.3',
    zipfile=None,
    data_files=data_files,
    windows=[
        {
            "script": "barion.py",
             'icon_resources': [(1, 'rsrc/icon.ico')]
        }
    ],
    options={
        "py2exe": {
            "includes":["sip", "atexit",],
            "compressed": True,
            "optimize": 2,
            'packages': ['fortranformat']
        }
    }
)
