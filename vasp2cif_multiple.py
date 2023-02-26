# this script exports multiple .vasp files in a directory to .cif files

from pymatgen.core import Structure
import os
import glob

# input directory containing .vasp files
direc_vasp = os.getcwd()+'/data'    # keep all the .vasp files in a directory named data

# output directory containing .cif files
os.mkdir('data_cif')   # creates a directory data_cif, where the cif files will the written
direc_cif  = os.getcwd()+'/data_cif'

os.chdir(direc_vasp)
for poscar_file in glob.glob("*.vasp"):          # searches for .vasp files in a directory 
    struct_name = os.path.splitext(poscar_file)  
    struct_name_wo_ext = struct_name[0]          # structure name without extension
    struct = Structure.from_file(poscar_file)    # reads a poscar file using pymatgen
    os.chdir(direc_cif)                          # change directory to direc_cif to write cif file
    struct.to(fmt='cif',filename=struct_name_wo_ext+'.cif') # saves the poscar file with cif extension
    os.chdir(direc_vasp)                         # changes directory to direc_vasp
