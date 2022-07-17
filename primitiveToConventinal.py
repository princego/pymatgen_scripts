from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
str = Structure.from_file('FILENAME') # Replace FILENAME with your filename
sga = SpacegroupAnalyzer(str)
conv = sga.get_conventional_standard_structure()
conv.to(fmt='poscar', filename='conventional') # Replace PRMITIVE with your desired filename
