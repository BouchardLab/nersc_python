#!/bin/bash -l
#SBATCH --qos=debug
#SBATCH --constraint=knl
#SBATCH --nodes=4
#SBATCH --time=00:05:00
#SBATCH --image=docker:jesselivezey/shifter_example:latest

# 4 KNL nodes for 5 minutes using shifter image

cores=1
export MKL_NUM_THREADS=$cores
export OMP_NUM_THREADS=$cores
export HDF5_USE_FILE_LOCKING=FALSE

# Running a job for 2 subjects that use 2 nodes each and 136 tasks each
#    file    nodes tasks            use shifter       local script       script options
srun -o s1.o -N 2  -n 136 -c $cores shifter python -u shifter_example.py /global/cfs/cdirs/m2043/jlivezey/S1.h5 &

srun -o s2.o -N 2  -n 136 -c $cores shifter python -u shifter_example.py /global/cfs/cdirs/m2043/jlivezey/S2.h5 &

wait
