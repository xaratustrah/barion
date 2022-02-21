# PyPI setup file

from setuptools import setup, find_packages
from barion.version import __version__
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

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
    description='A set of classes and a GUI for accessing information and perform calculations related to (relativistic or non-relativistic) ions and nuclei in accelerator storage rings.',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
