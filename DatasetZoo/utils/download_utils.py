import os
import requests
import sys
from clint.textui import progress
import h5py


def download_file(dataset, path_to_dataset,
                  source=None, login_details=None, overwrite=False):
    """Downloads a file from a specified base site

    """
    #########################################################
    # Handling the user input for what to do with the files #
    #########################################################
    if source is None:
        base = "https://s3.amazonaws.com/datasetzoo/datasests/"
    else:
        base = source  # The user has specified own dataset source
    data = base + dataset
    print("\nDownloading dataset. Might take a while\n")

    ######################################################
    # Actually downloading the file. Done using requests #
    ######################################################
    try:
        data = requests.get(data)
    except requests.ConnectionError as e:
        print("Could not download dataset {0} from {1}. \
        Error message: {2} ".format(dataset, base, e))
        sys.exit(1)

    #########################################################
    # Interesting part: technically we still save the file  #
    # regardless, it's just if they specify not to save, we #
    # throw it into dev/null                                #
    #########################################################
    with open("/dev/null", 'w') as f:
        total_length = int(data.headers.get('content-length'))
        for chunk in progress.bar(
                data.iter_content(chunk_size=1024),
                expected_size=(total_length / 1024) + 1):
            if chunk:
                    f.write(chunk)
                    f.flush()
    f = open(path_to_dataset + dataset, "w")
    f.write(data.content)
    f.close()

    data = h5py.File(path_to_dataset + dataset, "r")
    return data


def file_exists(dataset_name, save, overwrite, dataset_dir):
    """
    :p dataset_name: name of dataset to be downloaded
    :t dataset_name: string

    :p overwrite: whether the data should be overwritten. if not, we crash.
    :t overwrite: bool

    returns if the dataset_name file exists in the downloaded_datasets dir
    """
    if save is False:
        return False
    dataset_name = dataset_name
    if dataset_name in os.listdir(dataset_dir):
        if not(overwrite):
            raise FileExistsError
        else:
            return True
    else:
        return True
