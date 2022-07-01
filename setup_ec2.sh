# script to setup an EC2 instance with all the required libs

# define whether to install gpu related libs or not
type=$1

# initial update
sudo apt update
sudo apt upgrade -y
sudo apt install cmake -y

# python
if [ $(uname -m) == aarch64 ]; then
    wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-aarch64.sh
    bash Anaconda3-2022.05-Linux-aarch64.sh
else
    wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
    bash Anaconda3-2022.05-Linux-x86_64.sh
fi
anaconda3/bin/conda init bash

# gpu/cpu specific python libs - comment out unrequired libs
if [ $type == gpu ]; then
    anaconda3/bin/conda install pytorch torchvision cudatoolkit=11.3 -c pytorch
    anaconda3/bin/pip install lightgbm --install-option=--cuda
elif [ $type == cpu ]; then
    anaconda3/bin/conda install pytorch torchvision cpuonly -c pytorch
    anaconda3/bin/pip install lightgbm
else
    echo "please select either cpu or gpu install"
fi

# other python libs - comment out unrequired libs
anaconda3/bin/conda install numpy
anaconda3/bin/conda install pandas
anaconda3/bin/conda install seaborn
anaconda3/bin/conda install matplotlib
anaconda3/bin/conda install boto3
anaconda3/bin/conda install fastparquet
anaconda3/bin/conda install scipy
anaconda3/bin/conda install shapely
anaconda3/bin/conda install geopandas
anaconda3/bin/conda install fuzzywuzzy 
anaconda3/bin/conda install cython 
anaconda3/bin/conda install -c huggingface transformers
anaconda3/bin/conda install -c huggingface -c conda-forge datasets
anaconda3/bin/conda install -c conda-forge scikit-learn
anaconda3/bin/pip install wandb awscli numerapi

# setup wandb
wandb login

# configure aws cli
aws configure

