import os
import requests
import sys
from clint.textui import progress
import h5py


def download_file(dataset, save_to, path_to_dataset,
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
    if overwrite:
        try:
            os.remove(path_to_dataset + dataset + ".h5")
        except:
            pass

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
    f = open(save_to + dataset + ".h5", "w")
    f.write(data.content)
    f.close()

    data = h5py.File("test_h5.h5", "r")
    return data


def file_exists(dataset_name, save, overwrite, dir_dataset, dir_above):
    """
    :p dataset_name: name of dataset to be downloaded
    :t dataset_name: string

    :p overwrite: whether the data should be overwritten. if not, we crash.
    :t overwrite: bool

    returns if the dataset_name file exists in the downloaded_datasets dir
    """
    if save is False:
        return False
    dataset_name = dataset_name + ".h5"
    os.chdir(dir_dataset)
    try:
        os.mkdir(dir_above)
    except:
        pass
    if overwrite or dataset_name in os.listdir(dir_above):
        try:
            raise FileExistsError
        finally:
            print("The file already exists.\
            Either delete it, or specify an overwrite, or don't save it")
    else:
        return True
