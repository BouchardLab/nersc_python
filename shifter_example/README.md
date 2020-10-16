# Shifter example

For python jobs with many tasks, using Docker containers with [Shifter](https://docs.nersc.gov/development/shifter/how-to-use/) can make their startup much more efficient. There is much better documentation about Docker, Shifter, and Slurm elsewhere, but this contains a basic outline of the process to provide some understanding
of the example files/scripts.

In this example, we can use the image I've made from the included Dockerfile. If you need to make your own environment, you can roughly follow these steps.

On your local machine, edit and build the example Dockerfile

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

On a NERSC login node, pull the image into Shifter

```bash
shifterimg -v pull docker:username/my_image:latest
```
