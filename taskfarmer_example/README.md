# TaskFarmer example

[TaskFarmer](https://docs.nersc.gov/jobs/workflow/taskfarmer/) is a NERSC utility for managing large numbers of independent tasks. It is meant to be used in cases where each task takes minutes to hours to run.

Hyperparameter search for machine learning or deep learning models is one potential use-case. Here, we implement a random search for a Lasso model. `task_farmer_example.py` is a small script which takes a random seed as an input and fits a small model to some generated data. `wrapper.sh` specifies some environment variables that are needed and will be called by TaskFarmer. `run_taskfarmer_example.sh` runs the tasks.

`write_tasks.py` writes the `tasks.txt` file which is a list of tasks and seeds. This isn't an official part of the TaskFarmer pipeline, but it might make sense for you to script the generation of the file.

First `tasks.txt` must be created
```python
python write_tasks.py
```

then TaskFarmer needs to be loaded
```bash
module load taskfarmer
```

and finally, the job can be submitted
```bash
sbatch run_taskfarmer_example.sh
```
