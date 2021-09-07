# Base image to build off of
FROM jesselivezey/nersc_conda_3.7:latest
# Assumes .environment.yml has been copied to the same directory as the Dockerile
COPY ./environment.yml /home/environment.yml
RUN conda env update -f environment.yml

# Update pytorch
RUN conda update pytorch
RUN pip install pykalman
RUN pip install tqdm
# Dummy command line argument to clear rebuild cache
# Run with sudo docker build --build-arg cache_reset=??
ARG cache_reset=unknown
RUN git clone https://github.com/akumar01/DynamicalComponentsAnalysis
RUN git clone https://github.com/akumar01/PyUoI
RUN git clone https://github.com/akumar01/schwimmbad

# Time warping software
RUN git clone https://github.com/ahwillia/affinewarp/

# This branch of DCA does not import torch.fft, which doesn't seem to work
RUN cd /home/DynamicalComponentsAnalysis && git checkout nofft && pip install -e .
RUN cd /home/schwimmbad && pip install -e .
RUN cd /home/affinewarp && pip install -e .

# Switch to VAR branch
RUN cd /home/PyUoI && git checkout var && pip install -e .

# Entrypoint
ADD entrypoint.sh /home/entrypoint.sh
RUN chmod 777 /home/entrypoint.sh
#ENV TINI_VERSION v0.16.1
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini #/usr/bin/tini
#RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/bin/bash", "/home/entrypoint.sh"]
CMD [ "/bin/bash" ]
