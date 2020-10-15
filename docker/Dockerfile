FROM debian:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /home/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y build-essential gfortran wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

SHELL [ "/bin/bash", "--login", "-c" ]

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /home/conda && \
    rm ~/miniconda.sh && \
    /home/conda/bin/conda clean -tipsy && \
    ln -s /home/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /home/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

# Initializes conda
ENV PATH=/home/conda/bin:$PATH
# Install
RUN conda update -n base -c defaults conda
RUN conda install python=3.7
RUN conda install numpy scipy scikit-learn

WORKDIR /tmp

ARG mpich=3.3
ARG mpich_prefix=mpich-$mpich

RUN \
    wget https://www.mpich.org/static/downloads/$mpich/$mpich_prefix.tar.gz && \
    tar xvzf $mpich_prefix.tar.gz                                           && \
    cd $mpich_prefix                                                        && \
    ./configure                                                             && \
    make -j 4                                                               && \
    make install                                                            && \
    make clean                                                              && \
    cd ..                                                                   && \
    rm -rf $mpich_prefix

ARG mpi4py=3.0.0
ARG mpi4py_prefix=mpi4py-$mpi4py

RUN \
    wget https://bitbucket.org/mpi4py/mpi4py/downloads/$mpi4py_prefix.tar.gz && \
    tar xvzf $mpi4py_prefix.tar.gz                                           && \
    cd $mpi4py_prefix                                                        && \
    python setup.py build                                                   && \
    python setup.py install                                                 && \
    cd ..                                                                    && \
    rm -rf $mpi4py_prefix

RUN /sbin/ldconfig

WORKDIR /home

# Pull additional repos
RUN git clone https://github.com/BouchardLab/mpi_utils.git /home/mpi_utils

# Install additional repos
RUN pip install -e /home/mpi_utils

# Setup entrypoint
ADD entrypoint.sh /home/entrypoint.sh
RUN chmod 777 /home/entrypoint.sh
ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT [ "/usr/bin/tini", "--", "/home/entrypoint.sh" ]
CMD [ "/bin/bash" ]
