# !/usr/bin/env python
"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah

"""

from setuptools import setup

app=['barion.py']

version = '0.0.1'

pkgs = ['fortranformat']

includes = ['sip',
            'PyQt5',
            'PyQt5.QtWidgets',
            'PyQt5.QtCore',
            'PyQt5.QtGui']

options = {'argv_emulation': True,
           'includes': includes,
           'iconfile': 'icon.icns',
           'packages': pkgs}

datafiles = []

setup(
    app=app,
    name='barion',
    version=version,
    url='',
    license='',
    data_files=datafiles,
    options={'py2app': options},
    setup_requires=['py2app']
)
