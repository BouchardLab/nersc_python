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
RUN R -e "library(devtools); devtools::install_github('BouchardLab/ergm', build_vignettes=FALSE)"

# Install other required R packages
RUN R -e "install.packages(c('igraph', 'reticulate', 'intergraph'))"

# Install python, schwimmbad, and mpi4py
RUN apt-get update && apt-get install -y python3-dev python3-pip

# Note: Using the NERSC provided recipe
ARG mpich=4.0.2
ARG mpich_prefix=mpich-$mpich

RUN wget https://www.mpich.org/static/downloads/$mpich/$mpich_prefix.tar.gz
RUN    tar xvzf $mpich_prefix.tar.gz                                      
RUN    cd $mpich_prefix && ./configure FFLAGS=-fallow-argument-mismatch FCFLAGS=-fallow-argument-mismatch && \
        make -j 4 && make install && make clean
RUN /sbin/ldconfig
RUN python3 -m pip install mpi4py

RUN python3 -m pip install schwimmbad

# Entrypoint to run R script
# ADD entrypoint.sh /home/entrypoint.sh
# RUN chmod 777 /home/entrypoint.sh

# ENTRYPOINT [ "/bin/bash", '/home/entrypoint.sh' ]
# CMD ["/bin/bash"]