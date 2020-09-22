# Base docker image
FROM jesselivezey/nersc_conda_3.7:latest

# Install libraries with conda if needed/possible
RUN conda install h5py scikit-learn pytorch cpuonly -c pytorch -y

# Install libraries with pip if needed/possible
RUN pip install pynwb pyuoi

# Pull additional public repos
RUN git clone https://github.com/BouchardLab/process_nwb.git /home/process_nwb

# Add local private repo from your machine
ADD my_repo /home/my_repo

# Install additional repos
RUN pip install -e /home/process_nwb && pip install -e /home/spectrumregression
