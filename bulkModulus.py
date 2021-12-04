from pymatgen.analysis.eos import EOS
import numpy as np

energy = np.loadtxt('energyVol')[:,0] # reads energy
volume = np.loadtxt('energyVol')[:,1] # reads volume

bm = EOS(eos_name='birch_murnaghan')
bm_fit = bm.fit(volume, energy)
print(bm_fit.b0_GPa, 'Birch-Murnaghan')
print(bm_fit.results,'\n')

murnaghan = EOS(eos_name='murnaghan')
murnaghan_fit = murnaghan.fit(volume, energy)
print(murnaghan_fit.b0_GPa, 'Murnaghan')
print(murnaghan_fit.results,'\n')

birch = EOS(eos_name='birch')
birch_fit = birch.fit(volume, energy)
print(birch_fit.b0_GPa, 'Birch')
print(birch_fit.results,'\n')

vinet = EOS(eos_name='vinet')
vinet_fit = vinet.fit(volume, energy)
print(vinet_fit.b0_GPa, 'Vinet')
print(vinet_fit.results)
