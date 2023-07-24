from pymatgen.core import Structure
str = Structure.from_file("CONTCAR") # enter the filename in " "
supercell = str.copy()
supercell.make_supercell([2,2,2]) # makes a 2x2x2 supercell
supercell.to("POSCAR_supercell")
