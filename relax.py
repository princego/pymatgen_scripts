from pymatgen.core import Structure
from pymatgen.io.vasp.sets import MPRelaxSet

a=Structure.from_file("POSCAR")

user_incar = {'ISTART':0, 'ICHARG':None,'NELM':100, 'NSW':60, 'EDIFF':1E-5, 'PREC':'Accurate', 'ISPIN':None,\
              'LORBIT':None, 'LCHARG':'False', 'MAGMOM':None}

#user_kdensity = {"grid_density": 2000}
#b=MPRelaxSet(a, user_incar_settings = user_incar, user_kpoints_settings = user_kdensity)

b=MPRelaxSet(a, user_incar_settings = user_incar)
b.write_input(".")
