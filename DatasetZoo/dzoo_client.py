from utils.download_utils import __download_file
from utils.download_utils import __dataset_exists

"""
from utils.upload_utils import verify_type
from utils.upload_utils import verify_information
from utils.upload_utils import already_exists
from utils.upload_utils import _upload
"""


def download(dataset_name, save=True, overwrite=False,
             source=None, login_details=None):
    """
    Download dataset_name from source
    @TODO: support login details

    :param dataset_name: string: name of dataset to download. Include .h5
    :param save: bool: whether to save the data
    :param overwrite: bool: whether to overwrite if we find conflict
    :param source: string: valid url to download from
    :param login_details: dict : login details

    :returns: dataset
    :rtype: h5 instance

    returns a single h5py object which must have 4 top level groups
    1) description of the dataset, how to use
    2) X's -> test, train and validation if any (must be specified in 1)
    3) Y's -> test, train and validation if any (must be specified in 1)
    4) Misc -> any other objects that don't fall into the data. For example
    weights learning rates and so forth
    5) Special thanks: PI, Lab, University
    """
    import os
    curr_dir = os.path.dirname(__file__)
    dataset_dir = curr_dir + "/downloaded_datasets/"
    if not(__dataset_exists(dataset_name, save, overwrite, dataset_dir)):
        data = __download_file(dataset_name, dataset_dir,
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
    import h5py
    import os.path
    curr_dir = os.path.dirname(__file__)
    dataset_dir = curr_dir + "/downloaded_datasets/"
    try:
        f = h5py.File(dataset_dir + dataset_name, 'r')
        return f
    except:
        print("There was an error accessing the data. \n\
        Use list_installed_datasets to view what is installed locally\n\
        Else please download the appropriate dataset")
        return None


def list_source_datasets(source=None):
    """List out the datasets available for download from source

    :param source: valid url: where we check for files from
    :returns: None
    :rtype: None

    """
    import requests
    if source is None:
        base = "https://s3.amazonaws.com/datasetzoo/datasets/dataset_list.txt"
    else:
        base = source
    data = requests.get(base)
    for line in data.iter_lines():
        print(line)
    return


def list_local_datasets():
    """ List locally available datasets

    :returns: None
    :rtype: None
    """
    import os.path
    curr_dir = os.path.dirname(__file__)
    dataset_dir = curr_dir + "/downloaded_datasets/"
    if len(os.listdir(dataset_dir)) == 0:
        print("No datasets installed yet")
    else:
        for dataset in os.listdir(dataset_dir + dir):
            if ".py" not in dataset or ".pyc" not in dataset:
                print(dataset)
    return
