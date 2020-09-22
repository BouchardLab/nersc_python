# nersc_python
Docker images and example slurm scripts

## Docker image for use with [Shifter](https://docs.nersc.gov/development/shifter/how-to-use/)

The `docker` folder contains `Dockerfile` and `entrypoint.sh` files. `Dockerfile` specifies a basic [Python 3.7 conda-based python environment](https://hub.docker.com/repository/docker/jesselivezey/nersc_conda_3.7/general) which has the following standard scientific python libraries installed

 * TODO

along with NERSC compatible version of

 * TODO
 
 and an `mpi4py` [utilities library](https://github.com/BouchardLab/mpi_utils) the lab has developed.
 
 You can build python environments on top of this image for use for your projects. An example can be found at TODO.
 
 ## Slurm scripts
 
 There are many ways to use the HPC systems are NERSC. There are a few things to think about before starting 

Job types
 * Dependency
  * Independent tasks: computational-heavy hyperparameter search or scans, across-subject/condition analysis
  * Mildly-dependent jobs: read/write-heavy hyperparameter search, analysis summary scripts
  * Highly-dependent tasks: UoI, data- or model-parallel methods
 * Length (also consider the variability of tasks run lengths)
  * Short: a few seconds to a few minutes
  * Medium: 10s of minutes to an hours
  * Long: many hours
 * Size of job (number of tasks)
  * Small: <20
  * Medium: 20-100
  * Large: >100
 
Questions to ask before starting to write analysis code and Slurm scripts for use on NERSC
 * How many independent tasks do you want to run?
  * For less than 100 short/medium tasks, bash for-loops are often good enough. `mpi4py` is sometimes useful.
  * For many long tasks consider TaskFarmer, especially if they are very uneven in time. For many short/medium tasks `mpi4py`.
 * How long does each task take?
  * Long tasks can be run with loops or TaskFarmer without Shifter, short/medium should be run with `mpi4py` and Shifter (especially for large jobs).
 * Does a task require an entire node? More than 1 node? A fraction of a node?
  * If a task requires much less than 1 node, you'll need to use `mpi4py`.
 * Do the tasks share any large datasets that need to be read?
  * Having all tasks read the dataset will be less efficient than using `mpi4py` to distribute the data.
  * Reading the data many times (bash loops) will be less efficient than using `mpi4py` (sequentially).
 * How many hours will your job use in total?
  * <10k is meaningless
  * 10k-100k requires some care
  * >100k requires care
  * >1m should be carefully tested
 * How many times might you re-run the code?
  * <5 times with not many hours: just make things work
  * Otherwise: you should plan your code for use on NERSC
  
Some useful tools:
 * Bash for-loops (simple hyperparameter search/scanning)
 * [TaskFarmer](https://docs.nersc.gov/jobs/workflow/taskfarmer/) fancy hyperparameter search
 * [Shifter](https://docs.nersc.gov/development/shifter/how-to-use/): more efficient python on NERSC
