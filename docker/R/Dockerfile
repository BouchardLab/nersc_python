FROM debian:latest

# Dependencies
RUN apt-get update --fix-missing && \
    apt-get install -y build-essential ca-certificates wget gfortran
RUN apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common -y
RUN wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu66_66.1-2ubuntu2_amd64.deb
RUN apt update && dpkg -i libicu66_66.1-2ubuntu2_amd64.deb

RUN wget http://security.ubuntu.com/ubuntu/pool/main/libj/libjpeg-turbo/libjpeg-turbo8_2.0.3-0ubuntu1.20.04.3_amd64.deb
RUN apt update && dpkg -i libjpeg-turbo8_2.0.3-0ubuntu1.20.04.3_amd64.deb

RUN wget http://mirrors.kernel.org/ubuntu/pool/main/libj/libjpeg8-empty/libjpeg8_8c-2ubuntu8_amd64.deb
RUN apt update && dpkg -i libjpeg8_8c-2ubuntu8_amd64.deb

# # Install R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
RUN apt update && apt install r-base r-base-dev -y

# # Dependencies for devtools
RUN apt-get install libcurl4-gnutls-dev libxml2-dev libssl-dev libfontconfig1-dev libharfbuzz-dev libfribidi-dev \
    libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev -y
RUN R -e "install.packages('devtools',dependencies=TRUE, repos='http://cran.rstudio.com/')"

# Install ergm from github
ARG ERGM_UPDATE=unknown
RUN R -e "library(devtools); devtools::install_github('BouchardLab/ergm', build_vignettes=FALSE)"

# Install other required R packages
RUN R -e "install.packages(c('igraph', 'reticulate', 'intergraph'))"

WORKDIR /opt
# Install python and mpi4py
RUN \
    apt-get update        && \
    apt-get install --yes    \
        build-essential      \
        gfortran             \
        python3-dev          \
        python3-pip          \
        wget              && \
    apt-get clean all

# MPI4py - NERSC version
ARG mpich=4.0.2
ARG mpich_prefix=mpich-$mpich

RUN \
    wget https://www.mpich.org/static/downloads/$mpich/$mpich_prefix.tar.gz        && \
    tar xvzf $mpich_prefix.tar.gz                                                  && \
    cd $mpich_prefix                                                               && \
    ./configure FFLAGS=-fallow-argument-mismatch FCFLAGS=-fallow-argument-mismatch && \
    make -j 4                                                                      && \
    make install                                                                   && \
    make clean                                                                     && \
    cd ..                                                                          && \
    rm -rf $mpich_prefix

RUN /sbin/ldconfig

RUN python3 -m pip install mpi4py

RUN pip install numpy
RUN pip install scipy
RUN pip install rpy2
RUN pip install tqdm
RUN pip install pandas

# Install packages needed for fit_ergm.py
RUN pip install jax==0.4.14
RUN pip install jaxlib==0.4.11
RUN pip install ml_dtypes==0.2.0

# Install git
# AK had to do this manually
# Install motif counting

# RUN apt install git -y
# RUN git clone https://github.com/ComplexNetworks-DCC-FCUP/fase.git
# RUN /opt/fase/make

#WORKDIR /gtrieScanner
#RUN make
# Entrypoint to run R script
# ADD entrypoint.sh /home/entrypoint.sh
# RUN chmod 777 /home/entrypoint.sh

# ENTRYPOINT [ "/bin/bash", '/home/entrypoint.sh' ]
# CMD ["/bin/bash"]
