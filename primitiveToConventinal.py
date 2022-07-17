from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
str = Structure.from_file('filename') # Replace filename with your structure file name
sga = SpacegroupAnalyzer(str)
conv = sga.get_conventional_standard_structure()
conv.to(fmt='poscar', filename='conventional') # Replace conventional with your desired conventional cell filename
