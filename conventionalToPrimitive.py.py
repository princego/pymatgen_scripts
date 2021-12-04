from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
str = Structure.from_file('FILENAME') # Replace FILENAME with your filename
strPrim = str.get_primitive_structure()
strPrim.to(fmt='poscar', filename='PRIMITIVE') # Replace PRMITIVE with your desired filename
