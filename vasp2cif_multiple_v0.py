# this script exports multiple .vasp files in a directory to .cif files

from pymatgen.core import Structure
import os
import glob

direc_vasp = '/Users/abc/poscars/' # have all the .vasp files here
direc_cif  = '/Users/abc/poscars_cif/'
os.chdir(direc_vasp)

for poscar_file in glob.glob("*.vasp"):
    struct_name = os.path.splitext(poscar_file)
    struct_name_wo_ext = struct_name[0]
    struct = Structure.from_file(poscar_file)
    os.chdir(direc_cif)
    struct.to(fmt='cif',filename=struct_name_wo_ext+'.cif')
    os.chdir(direc_vasp)
