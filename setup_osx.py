# !/usr/bin/env python
"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""

from version import __version__
from setuptools import setup

app = ['barion.py']

pkgs = ['fortranformat']

includes = ['sip',
            'PyQt5',
            'PyQt5.QtWidgets',
            'PyQt5.QtCore',
            'PyQt5.QtGui']

options = {'argv_emulation': True,
           'includes': includes,
           'iconfile': 'rsrc/icon.icns',
           'packages': pkgs}

data_files = []

setup(
    app=app,
    name='barion',
    version=__version__,
    url='https://github.com/xaratustrah/barion',
    license='GPLv.3',
    data_files=data_files,
    options={'py2app': options},
    setup_requires=['py2app'],
)
