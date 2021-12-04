from pymatgen.core import Structure
a=Structure.from_file('CONTCAR') #you can replace CONTCAR with your filename
print(a.volume)
