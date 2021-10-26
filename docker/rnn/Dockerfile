# Base image to build off of
FROM jesselivezey/nersc_conda_3.7:latest
# Assumes .environment.yml has been copied to the same directory as the Dockerile
# Also assumes the environment is the base environment
COPY ./environment.yml /home/environment.yml
RUN conda env update -f environment.yml

# Dummy command line argument to clear rebuild cache
# Run with sudo docker build --build-arg cache_reset=??
ARG cache_reset=unknown

RUN git clone https://github.com/akumar01/schwimmbad.git

# This is a private repository, so it needs to be copied rather than cloned
# Need to run sudo mount -o bind ~/nse/RNN rnn_repo/ to create a symbolic link
# Make sure that RNN repo is swithched to MPI branch
COPY /rnn_repo /home/rnn

RUN cd /home/schwimmbad && pip install -e .
RUN cd /home/rnn && pip install -e .

# Entrypoint
ADD entrypoint.sh /home/entrypoint.sh
RUN chmod 777 /home/entrypoint.sh
#ENV TINI_VERSION v0.16.1
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini #/usr/bin/tini
#RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/bin/bash", "/home/entrypoint.sh"]
CMD [ "/bin/bash" ]
