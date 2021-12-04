# This script reads POSCAR file and gives space group information, including wyckoff positions
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer as sga
pos=Structure.from_file("POSCAR") # Replace POSCAR with your filename
print("POSCAR",pos.get_space_group_info(), sga.get_crystal_system(sga(pos)))
print(sga.get_symmetrized_structure(sga(pos)))
