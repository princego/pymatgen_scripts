# this scripts converts any CONTCAR or POSCAR file into a POSCAR file with the same filename
from pymatgen.core import Structure
import os
import glob

os.chdir('/Users/abc/data') # give the path to the directory where .vasp files are stored
poscar_files = glob.glob('*') # if you want files with .vasp extension, type glob.glob('*.vasp')

for i in poscar_files:
    os.chdir('/Users/abc/data')
    str = Structure.from_file(i)
    os.chdir('/Users/abc/dataNew')
    str.to(fmt='poscar', filename=i)
