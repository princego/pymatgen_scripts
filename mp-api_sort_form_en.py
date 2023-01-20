from mp_api.client import MPRester
mpr = MPRester('<your api key>') # get it in materials project dashboard after signing up.

# collecting mp ids for Hf-C based materials
HfC_mp = mpr.get_materials_ids('Hf-C')

# collecting formation energy per atom
HfC_dict={}
for i in range(len(HfC_mp)):
    HfC_form_en = mpr.get_entry_by_material_id(HfC_mp[i].strip(), property_data=['formation_energy_per_atom'])[0].data['formation_energy_per_atom']
    HfC_dict.update({HfC_mp[i].strip():HfC_form_en})

# sorting according to least formation energy per atom
sorted_dict = dict(sorted(HfC_dict.items(), key=lambda x:x[1]))
print(sorted_dict)
