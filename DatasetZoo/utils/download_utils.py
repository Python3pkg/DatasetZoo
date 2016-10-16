import os
import requests


def download_file(dataset, source=None, login_details=None):
    """Downloads a file from a specified base site

    :param dataset: dataset name to download from source
    :param source: valid HTML source
    :param login_details: dict containing login + password
    :returns: the requested dataset, or a failure
    :rtype: h5 file

    """
    if source is None:
        base = "http://"
    else:
        base = source
    data = base + dataset
    print("\nDownloading dataset. Might take a while\n")
    try:
        data = requests.get(data)
    except requests.ConnectionError as e:
        print("Could not download dataset {0} from {1}. Error message: {2}\
        ".format(dataset, base, e))
    print("Finished downloading\n")
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
        continue
    if overwrite or dataset_name in os.listdir(dir_above):
        try:
            raise FileExistsError
        finally:
            print("The file already exists.\
            Either delete it, or specify an overwrite, or don't save it")
    else:
        return True


def save_dataset(dataset_name, data, overwrite, path_to_dataset):
    """
    :p dataset_name name to save the dataset as
    :t dataset_name string

    :p data h5py file
    :t data h5py file

    :p overwrite whether we should overwrite any currently existing
    datasets with the same name
    :t overwrite bool
    """
    dataset_name = dataset_name + ".h5"
    os.chdir(path_to_dataset)
    if overwrite:
        os.remove(dataset_name)
    with open(dataset_name, "wb") as code:
        code.write(data.content)
