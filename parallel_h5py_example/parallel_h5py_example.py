import h5py
import numpy as np
from mpi4py import MPI


# Setup MPI sizes
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# All ranks for file creation
with h5py.File('parallel_test.h5', 'w', driver='mpio', comm=comm) as f:
    # All ranks for dataset or group creation
    data = f.create_dataset('test', (size,), dtype=int)

    # All ranks can write
    data[rank] = rank
    # Single ranks can write
    if rank == 0:
        data[rank] = -1
