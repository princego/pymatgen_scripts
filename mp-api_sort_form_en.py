from mp_api.client import MPRester
mpr = MPRester('<your api key>') # get it in materials project dashboard after signing up.

# collecting mp ids
structures = 'Hf-C' # here we get Hf-C based structures
mp_ids = mpr.get_materials_ids(structures)

# collecting formation energy per atom
structure_dict={}
for i in range(len(mp_ids)):
    form_en = mpr.get_entry_by_material_id(mp_ids[i].strip(), property_data=['formation_energy_per_atom'])[0].data['formation_energy_per_atom']
    structure_dict.update({mp_ids[i].strip():form_en})

# sorting according to least formation energy per atom
sorted_dict = dict(sorted(structure_dict.items(), key=lambda x:x[1]))
# print(sorted_dict)

# finding bulk and shear modulus for the lowest formation energy structure
material = mpr.elasticity.get_data_by_id(list(sorted_dict.keys())[0])
data = {'system':material.pretty_formula,'bulk_modulus':material.elasticity.k_vrh, 'shear_modulus':material.elasticity.g_vrh, list(sorted_dict.keys())[0]: list(sorted_dict.values())[0]}
print(data)
