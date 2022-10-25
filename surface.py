from pymatgen.core import Structure
from pymatgen.core.surface import SlabGenerator
a = Structure.from_file("CONTCAR") #change to your filename
b = SlabGenerator(a, [1,1,1], 10, 10) #10, 10 are min slab size and min vacuum
slab.to(fmt="POSCAR", filename="surface_111.vasp")
