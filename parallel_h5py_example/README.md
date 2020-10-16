# Parallel h5py write example

If many mpi ranks need to write to a file in parallel, you'll need to use the h5py built for parallel mpi write. If you only need parallel read, you just need to set file locking and open the file with the 'r' attribute.

After you run this script, you can inspect the output file or the h5 file.
