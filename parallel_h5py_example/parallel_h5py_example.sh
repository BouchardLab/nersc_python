#!/bin/bash -l
#SBATCH --qos=debug
#SBATCH --constraint=knl
#SBATCH --nodes=1
#SBATCH --time=00:05:00
#SBATCH --image=docker:jesselivezey/nersc_conda_3.7:latest

# 1 KNL node for 5 minutes using shifter image

cores=1
export MKL_NUM_THREADS=$cores
export OMP_NUM_THREADS=$cores
export HDF5_USE_FILE_LOCKING=FALSE

# Running a job with 68 tasks
#    file    nodes tasks            use shifter       local script       script options
srun -N 1  -n 68 -c $cores shifter python -u parallel_h5py_example.py

module load cray-hdf5-parallel
h5dump parallel_test.h5
