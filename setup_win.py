from distutils.core import setup
#!/usr/bin/env python
"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah

"""

import py2exe

VERSION='0.0.1'

PKG = ['fortranformat']

includes = ['sip',
			'PyQt5',
			'PyQt5.QtWidgets',
			'PyQt5.QtCore',
			'PyQt5.QtGui']

datafiles = [("platforms", ["C:\\Python34\\Lib\\site-packages\\PyQt5\\plugins\\platforms\\qwindows.dll"]),
			("", [r"c:\windows\syswow64\MSVCP100.dll", r"c:\windows\syswow64\MSVCR100.dll"])]

setup(
	name='barion',
    version=VERSION,
	url='',
	license='',
	zipfile=None,
	data_files=datafiles,
	windows=[{
			'script': 'barion.py',
			'icon_resources': [(1, 'icon.ico')],
			'dest_base':'barion'
			}], 
	options={'py2exe':{
		'bundle_files': 1,
		'compressed': True,
		'includes': includes, 
		'packages': PKG
		}})
