from utils.download_utils import download_file
from utils.download_utils import file_exists

"""
from utils.upload_utils import verify_type
from utils.upload_utils import verify_information
from utils.upload_utils import already_exists
from utils.upload_utils import _upload
"""

import h5py
import os
import requests
import os.path


def download(dataset_name, save=True, overwrite=False,
             source=None, login_details=None):
    """
    :p dataset_name name of the dataset to be downloaded
    :t dataset_name string

    :p save whether the downloaded dataset should be saved.
    :t save bool

    :p overwrite whether we should overwrite an existing local
    dataset
    :t overwrite bool

    returns a false indicating that the dataset couldn't be downloaded
    or the data itself as a dictionary

    returns a single h5py object which must have 4 top level groups
    1) description of the dataset
    2) X's -> test, train and validation if any (must be specified in 1)
    3) Y's -> test, train and validation if any (must be specified in 1)
    4) Misc -> any other objects that don't fall into the data. For example
    weights learning rates and so forth
    """
    curr_dir = os.path.dirname(__file__)
    dataset_dir = curr_dir + "/downloaded_datasets/"
    if not(file_exists(dataset_name, save, overwrite, dataset_dir)):
        data = download_file(dataset_name, dataset_dir,
                             source, login_details, save)
        return data
    # ENDIF: should never hit here as we'll error out within download_utils


# def upload(dataset_name, h5py_instance):
#     """
#     :p dataset_name name of the dataset to be downloaded
#     :t dataset_name string
#     Saves a dataset to the database if it doesn't exist
#     1) check it against the list of all datasets we have
#     2) if it exists, do nothing, and say that the dataset probably exists.
#       Email dev to update or whatever
#     3) If doesn't exist, write it to the ref file

#     Takes in a dataset name to save it as, and a h5py instance
#     which must fulfill the requirements above
#     """
#     if verify_type(h5py_instance) and verify_information(h5py_instance):
#         if not already_exists:
#             _upload(dataset_name, h5py_instance)
#             print("Uploading successful")
#         else:
#             print("File already exists, please email the maintainer if you\
#             have any questions")
#     else:
#         print("Please either convert the file type to a hdf5 file type,\
#         and make sure that it follows the predefined format")


def load_dataset(dataset_name):
    """
    :p dataset HDF5 file, which we save to disk
    :t dataset string name

    returns the dataset
    """
    curr_dir = os.path.dirname(__file__)
    dataset_dir = curr_dir + "/downloaded_datasets/"
    try:
        f = h5py.File(dataset_dir + dataset_name, 'r')
        return f
    except:
        print("There was an error accessing the data. Please\
        the list_local_datasets function to view what is installed\
        Else please download the appropriate dataset")
        return None


def list_datasets(source=None):
    if source is None:
        base = "https://s3.amazonaws.com/datasetzoo/datasets/dataset_list.txt"
    else:
        base = source
    data = requests.get(base)
    for line in data.iter_lines():
        print(line)
    return


def list_installed_datasets():
    curr_dir = os.path.dirname(__file__)
    dataset_dir = curr_dir + "/downloaded_datasets/"
    for dataset in os.listdir(dataset_dir):
        print(dataset)
    return
