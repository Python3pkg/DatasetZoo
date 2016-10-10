from utils.download_utils import download_file
from utils.download_utils import file_exists
from utils.download_utils import save_dataset
import h5py
import os
import urllib2


def download(dataset_name, save=True, overwrite=False):
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
    if not (file_exists(dataset_name, save, overwrite)):
        data = download_file(dataset_name)
        if save:
            save_dataset(dataset_name, data, overwrite)
        return (h5py.File(data, 'r'))
    # ENDIF: should never get here as exception will be raised


def upload(dataset_name, h5py_instance):
    """
    :p dataset_name name of the dataset to be downloaded
    :t dataset_name string
    Saves a dataset to the database if it doesn't exist
    1) check it against the list of all datasets we have
    2) if it exists, do nothing, and say that the dataset probably exists.
      Email dev to update or whatever
    3) If doesn't exist, write it to the ref file

    Takes in a dataset name to save it as, and a h5py instance
    which must fulfill the requirements above
    """
    pass


def load_dataset(dataset_name):
    """
    :p dataset HDF5 file, which we save to disk
    :t dataset string name
    """
    dataset_name = dataset_name + ".h5"
    curr_dir = os.getcwd()
    dataset_dir = curr_dir + "/downloaded_datasets"
    try:
        f = h5py.File(dataset_dir + dataset_name, 'r')
        return f
    except:
        print("There was an error accessing the data. Please\
        the list_local_datasets function to view what is installed\
        Else please download the appropriate dataset")
        return None


def list_datasets():
    base = "http://"
    data = urllib2.urlopen(base)
    for line in data:
        print(line)
    # Shouldn't have any access errors just because we're reading
    # from a file but keep an eye on this
    return


def list_local_datasets():
    curr_dir = os.getcwd()
    dataset_dir = curr_dir + "/downloaded_datasets"
    for dataset in os.listdir(dataset_dir):
        print(dataset)
    return
