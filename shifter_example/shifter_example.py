import numpy as np
from itertools import product
from argparse import ArgumentParser
from mpi4py import MPI


# Parse arguments
parser = ArgumentParser()
parser.add_argument('data', type=str, help='The input h5 file')
data = parser.data

# Setup MPI sizes
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# Analysis across channels and time
n_channels = 64
n_time = 100


# Typically, this function would be in a module
def analysis(file, ch_idx, time_idx):
    # Load some data
    # Do some analysis
    # Save some results
    print('Rank: {}, ch: {}, time: {}, {}'.format(rank, ch_idx, time_idx, file))
    return


# Select tasks for this rank
args = list(product([data], np.arange(n_channels), np.arange(n_time)))
args = np.array(args, dtype=object)
my_args = np.array_split(args, size)[rank]

# Run this rank's tasks
for arg in args:
    analysis(*arg)
