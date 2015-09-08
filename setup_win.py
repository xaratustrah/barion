# !/usr/bin/env python
"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah

"""

from distutils.core import setup
import py2exe

name = 'barion'

version = '0.0.1'

pkgs = ['fortranformat']

includes = ['sip',
            'PyQt5',
            'PyQt5.QtWidgets',
            'PyQt5.QtCore',
            'PyQt5.QtGui']

options = {'bundle_files': 1,
           'compressed': True,
           'includes': includes,
           'packages': pkgs
           }

datafiles = [("platforms", ["C:\\Python34\\Lib\\site-packages\\PyQt5\\plugins\\platforms\\qwindows.dll"]),
             ("", [r"c:\windows\syswow64\MSVCP100.dll", r"c:\windows\syswow64\MSVCR100.dll"])]

setup(
    name=name,
    version=version,
    url='',
    license='',
    zipfile=None,
    data_files=datafiles,
    windows=[{
        'script': 'barion.py',
        'icon_resources': [(1, 'icon.ico')],
        'dest_base': 'barion'
    }],
    options={'py2exe': options}
)
