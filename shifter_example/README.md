# Shifter example

For python jobs with many tasks, using Docker containers with [Shifter](https://docs.nersc.gov/development/shifter/how-to-use/) can make their startup much more efficient. There is much better documentation about Docker, Shifter, and Slurm elsewhere, but this contains a basic outline of the process to provide some understanding
of the example files/scripts.

On your local machine build the example Dockerfile

```bash
docker build --no-cache -t "my_image" .
```

Tag the image (`latest` is common if you're not being careful with versions)

```bash
docker tag my_image username/my_image:latest
```

Push the image to your Docker Hub

```bash
docker push username/my_image:tag
```

On a NERSC login node

```bash
shifterimg -v pull docker:username/my_image:latest
```

Now, `shifter_example.sh` can be used.