# Torch-CPD

Pytorch Implementation of the Coherent Point Drift Algorithm.



## Introduction

This is a PyTorch re-implementation of the excellent [pycpd](https://github.com/siavashk/pycpd) package, which implements the [Coherent Point Drift (CPD)](https://arxiv.org/abs/0905.2635/) algorithm. Only Rigid and Deformable Registration and currently implemented. The default is to use CUDA to speed up computation, which is significantly faster than pure Numpy. Refer to the [pycpd](https://github.com/siavashk/pycpd) package for examples of how to use CPD for registration. 

## Installation

### Install from PyPI

**You should install torch separately, follow instructions at https://pytorch.org/get-started/locally/**


``` bash
pip install torchcpd
```

### Installation from Source
``` bash
git clone https://github.com/ramtingh/torchcpd.git $HOME/torchcpd
```

Install the package:

``` bash
pip install .
```