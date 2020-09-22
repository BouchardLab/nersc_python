#!/bin/bash -l
#SBATCH --qos=regular
#SBATCH --constraint=knl
#SBATCH --nodes=200
#SBATCH --time=02:00:00
#SBATCH --image=docker:username/my_image:latest

# 200 KNL nodes for 2 hours using shifter image

cores=2
export MKL_NUM_THREADS=$cores
export OMP_NUM_THREADS=$cores
export HDF5_USE_FILE_LOCKING=FALSE

# Running a job for 4 subjects that use 50 nodes each and 1000 tasks each
#    file    nodes tasks             use shifter       local script       script options
srun -o s1.o -N 50 -n 1000 -c $cores shifter python -u shifter_example.py /global/cfs/cdirs/m2043/jlivezey/S1.h5 &

srun -o s2.o -N 50 -n 1000 -c $cores shifter python -u shifter_example.py /global/cfs/cdirs/m2043/jlivezey/S2.h5 &

srun -o s3.o -N 50 -n 1000 -c $cores shifter python -u shifter_example.py /global/cfs/cdirs/m2043/jlivezey/S3.h5 &

srun -o s4.o -N 50 -n 1000 -c $cores shifter python -u shifter_example.py /global/cfs/cdirs/m2043/jlivezey/S4.h5 &

wait
