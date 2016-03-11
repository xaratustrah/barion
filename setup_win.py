#!/usr/bin/env python
"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""

import py2exe
from distutils.core import setup
from version import __version__

name = 'barion'

pkgs = ['fortranformat']

includes = ['sip',
            'PyQt5',
            'PyQt5.QtWidgets',
            'PyQt5.QtCore',
            'PyQt5.QtGui']

excludes = ['pkg_resources',
            'doctest',
            'pdb',
            'optparse',
            'jsonschema',
            'tornado',
            'setuptools',
            'urllib2',
            'tkinter']

options = {'bundle_files': 1,
           # 'optimize': 2,
           'compressed': True,
           'includes': includes,
           'excludes': excludes,
           'packages': pkgs
           }

datafiles = [("platforms", ["C:\\Python34\\Lib\\site-packages\\PyQt5\\plugins\\platforms\\qwindows.dll"]),
             ("", [r"c:\windows\syswow64\MSVCP100.dll", r"c:\windows\syswow64\MSVCR100.dll"])]

setup(
    name=name,
    version=__version__,
    url='https://github.com/xaratustrah/barion',
    license='GPLv.3',
    zipfile=None,
    data_files=datafiles,
    windows=[{
        'script': 'barion.py',
        'icon_resources': [(1, 'icon.ico')],
        'dest_base': name
    }],
    options={'py2exe': options}
)
