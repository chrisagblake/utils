# script to setup an EC2 instance with the anaconda version of python

sudo apt update
if [ $(uname -m) == aarch64 ]; then
    wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-aarch64.sh
    bash Anaconda3-2022.05-Linux-aarch64.sh
else
    wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
    bash Anaconda3-2022.05-Linux-x86_64.sh
fi
anaconda3/bin/conda init bash

