#!/bin/sh
#SBATCH -N 2 -c 64
#SBATCH --qos=debug
#SBATCH --time=00:05:00
#SBATCH --constraint=knl
#SBATCH --image=docker:jesselivezey/nersc_conda_3.7:latest


cd $HOME/nersc_python/taskfarmer_example
export THREADS=32

runcommands.sh tasks.txt

