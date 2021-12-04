# This file prints final energy and energy per atom
from pymatgen.io.vasp.outputs import Vasprun
a=Vasprun("vasprun.xml")
print("===============================")
print("final energy = ", a.final_energy)
print("===============================")
print(a.get_computed_entry())
