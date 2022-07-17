from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
str = Structure.from_file('filename') # Replace filename with your structure file name
strPrim = str.get_primitive_structure()
strPrim.to(fmt='poscar', filename='primitive') # Replace primitive with your desired output filename
