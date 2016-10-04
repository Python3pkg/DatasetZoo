Dataset Zoo

A project that exists to make it easier for researchers to download different datasets and integrate it into their testing without needing the backend of a full model.

The main idea of this projecet is to provide a lightweight system that enables researchers to download datasets via the use of a simple, dependency light system. Also, this project aims to meet the goal of allowing researchers to easily share their projects with the rest of the community: simply use the Dataset_zoo.dataset_upload function to store it on our servers (HDF5 only please, you can use the from_pkl_convert() function to convert from a pkl file to HDF5)

Usage:

import Dataset_zoo

or

from Dataset_zoo import dataset_download(<supported dataset name>)
