#!/usr/bin/env bash

# Install conda packages
export PATH="$HOME/miniconda3_$TRAVIS_OS_NAME/bin:$PATH"
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
conda install --yes \
    abyss \
    biopython \
    bedtools \
    pandas \
    networkx
conda clean --all --yes

# SDSL-lite


# https://hub.docker.com/r/adamnovak/sequence-graphs/~/dockerfile/
if [[ ! test -e $HOME/sdsl-lite ]]; then
    git clone https://github.com/simongog/sdsl-lite.git
fi
pushd sdsl-lite && \
sudo ./install.sh /usr/local && \
popd

# biobloomtools
# as in https://github.com/bcgsc/biobloom
if [[! test -e $HOME/biobloom ]]; then
    git clone https://github.com/bcgsc/biobloom.git && \
fi
pushd biobloom/ && \
git submodule update --init && \
./autogen.sh && \
./configure --prefix=/usr/local && \
make -j 2 && \
sudo make install && \
popd
