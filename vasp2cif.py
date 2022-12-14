# this code reads POSCAR files with .vasp extension and exports with .cif extension
from pymatgen.core import Structure
import os
poscar_file = 'POSCAR.vasp' # enter your filename here
struct_name = os.path.splitext(poscar_file)
struct_name_wo_ext = struct_name[0]

struct = Structure.from_file(poscar_file)
struct.to(fmt='cif',filename=struct_name_wo_ext+'.cif')
