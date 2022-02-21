# PyPI setup file

from setuptools import setup, find_packages
from barion.version import __version__

long_description = ''

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

print(long_description)

classifiers = [
    'Environment :: X11 Applications :: Qt',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Topic :: Scientific/Engineering :: Physics',
    'Intended Audience :: Science/Research',
]

setup(
    name='barion',
    packages=find_packages(),
    version=__version__,
    description='A qt-based GUI program that offers a graphical interface to visually inspect the data processed by the iqtools library.',
    long_description=long_description,
    author='xaratustrah',
    url='https://github.com/xaratustrah/barion',  # use the URL to the github repo
    download_url='https://github.com/xaratustrah/barion/tarball/{}'.format(
        __version__),
    entry_points={
        'console_scripts': [
            'barion = barion.__main__:main'
        ]
    },
    license='GPLv3',
    keywords=['physics', 'atomic', 'mass', 'ion',
              'accelerators'],  # arbitrary keywords
    classifiers=classifiers
)
