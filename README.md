# barion
<sup> (c) Copyright M. Shahab SANJARI 2015-2016 </sup>

![barion](https://raw.githubusercontent.com/xaratustrah/barion/master/rsrc/screenshot.png)

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


#### Binary releases

Binary releases are available in the release section.


### Build / Run Prerequisites

**barion** is writen in Python 3.4 so it needs a standard working environment such as Linux, 
OSX or Windows. More general info on python installation under Win and OSX can be found on this [gist](https://gist.github.com/xaratustrah/4efc5001f1bbcce47e02e2343ba29b87). It should work out of the box
with standard linux installations. **barion** needs the library **fortranformat** which can 
be installed using **pip** pacakge manager.


## Acknowledgements
I am thankful to [carlkl](https://github.com/carlkl) for his valuable help in making a stand alone binary under MS Windows and also for fruitful discussions and suggestions.

