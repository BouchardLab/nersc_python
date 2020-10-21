n_tasks = 100

with open('tasks.txt', 'w') as f:
    f.write('#!/usr/bin/env bash\n\n')
    for ii in range(n_tasks):
        f.write('$HOME/nersc_python/taskfarmer_example/wrapper.sh {}\n'.format(ii))

