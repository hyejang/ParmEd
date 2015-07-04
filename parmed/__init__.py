"""
The parmed package manipulates molecular structures and provides a way to go
between standard and amber file formats, manipulate structures, etc.
"""

__version__ = '2.0beta3'
__author__ = 'Jason Swails'

from parmed import (exceptions, periodic_table, residue, unit, utils, formats,
                    amber, charmm, gromacs, tinker, openmm, rosetta)
from parmed.topologyobjects import *
from parmed.structure import Structure
from parmed.vec3 import Vec3
from parmed.parameters import ParameterSet
load_file = formats.load_file
read_PDB = formats.PDBFile.parse
read_CIF = formats.CIFFile.parse
write_PDB = formats.PDBFile.write
write_CIF = formats.CIFFile.write
load_rosetta = rosetta.RosettaPose.load

download_PDB = formats.PDBFile.download
download_CIF = formats.CIFFile.download
