import time
import numpy as np
from itertools import product
from argparse import ArgumentParser
from mpi4py import MPI
from mpi_utils.ndarray import Bcast_from_root, Gatherv_rows


# Parse arguments
parser = ArgumentParser()
parser.add_argument('fname', type=str, help='The input h5 file')
args = parser.parse_args()
fname = args.fname

# Setup MPI sizes
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# Analysis across channels and time
n_channels = 64
n_time = 100


# Typically, this function would be in a module
def analysis(data, fname, ch_idx, time_idx):
    # Load some data
    # Do some analysis
    # Save some results
    print('Rank: {}, ch: {}, time: {}, {}'.format(rank, ch_idx, time_idx, fname))
    return data.mean(axis=0)

# Generate data on root and broadcast
data = None
if rank == 0:
    data = np.arange(10).reshape(5, 2)
data = Bcast_from_root(data, comm, root=0)
data *= rank

# Select tasks for this rank
args = list(product([fname], np.arange(n_channels), np.arange(n_time)))
args = np.array(args, dtype=object)
my_args = np.array_split(args, size)[rank]

# result array for this rank
result = np.zeros((len(my_args), data.shape[1]))

# Run this rank's tasks
for ii, arg in enumerate(my_args):
    result[ii] = analysis(data, *arg)

# Gather result from all ranks to root
result = Gatherv_rows(result, comm, root=0)
time.sleep(1)
if rank == 0:
    print(result)
