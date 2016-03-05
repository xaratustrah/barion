# barion
<sup> (c) Copyright M. Shahab SANJARI 2015-2016 </sup>

![barion](https://raw.githubusercontent.com/xaratustrah/barion/master/screenshot.png)

## About

**barion** is a set of classes and also a graphical user interface written entirely in Python to access information and perform calculations related to (relativistic or non-relativistic) ions and nuclei. In essence, this program provides a convenient interface to the published data on atomic masses in the world famous  **Atomic Mass Evaluation by G. Audi and colleagues** from [G. Audi et al 2012 Chinese Phys. C 36 1287](http://dx.doi.org/10.1088/1674-1137/36/12/003).

  Specifically this program can be used in experiments involving mass and lifetime measurements of radioactive ion beams. It can also be used in a variety of applications such as medical radio therapy, astrophysics and fundamental physics research, etc. One can perform

- Identification of nuclides 
- Settings of accelerator parameters specially the storage rings
- Design and analysis of beam monitors specially Schottky detectors
- And many more...

## License

**barion** is free software: you can redistribute it and/or modify it under the 
terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version.

**barion** is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
**barion**.  If not, see <http://www.gnu.org/licenses/>.

The **AME2012 database** is not included with the distribution. It can be downloaded on demand within the software if not available.

This program makes NO CLAIMS OF CORRECTNESS OF THE DATA AND CALCULATION VALUES WHAT SO EVER.


## Running the code

### Binary releases
For some versions, binary releases for OSX and Win will be provided on GitHUB.
An Arch linux package is planned and will be announced.

### Build / Run Prerequisites

**barion** is writen in Python 3.4 so it needs a standard working environment such as Linux, 
OSX or Windows. It should work out of the box
with standard linux installations. **barion** needs the library **fortranformat** which can 
be installed using **pip** pacakge manager. **PyQt5** on the other hand should be installed
 separately because it contains many binary bindings.
 
 
#### OSX and Lin

Under OSX standard macports installation of python 3.4 and also via macports the PyQt5. 
The rest is obvious. Under linux you should as well be able to use your distribution's
package manager easily.

#### Win

It is possible to run and even make a binary file using py2exe under Win. I tested this 
using Win7 64 bit. On a blank Win machine download and install **Python 3.4.0** and 
**PyQt5.5.0** both x64 versions.
Note  that version numbers are important, because otherwise they will not match. 
Using **pip** you should then install

    pip install fortranformat py2exe

then you write

    python setup_win.py py2exe
    
then you should get a binary code.

#### Miniconda / Anaconda

Unfortunately PyQt5 is not yet supported in the main channel. But it can be installed from various channels.
 I have not tested it yet because I couldn't match the versions though. Anyone who makes it
 please leave a line here for info.
 
 