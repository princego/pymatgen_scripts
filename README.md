# Pymatgen Scripts
Converting a conventional cell to primitve cell.

##Running python scripts on supercomputers

Write the below command in the terminal to load python module

`module load anaconda3_2019`

input file

```

```

Submission script <br>
File: job.sh
```
#!/bin/bash
#PBS -o out
## Merge output and error files
#PBS -j oe
#PBS -k eod
#PBS -l walltime=00:59:59
## Select n nodes, each with n CPUs
#PBS -l select=1:ncpus=1
cd $PBS_O_WORKDIR
mpirun -np 1 /lfs/sware/anaconda3_2019/bin/python3 1.py > log
```

Submit the calculation
`qsub job.sh`
