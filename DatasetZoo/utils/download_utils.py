import os
import requests


def download_file(dataset):
    base = "http://"
    data = base + dataset
    print("\nDownloading dataset. Might take a while\n")
    data = requests.get(data)
    print("Finished downloading\n")
    return data


def file_exists(dataset_name, save, overwrite):
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
    curr_dir = os.getcwd()
    dir_above = curr_dir + "/downloaded_datasets"
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


def save_dataset(dataset_name, data, overwrite):
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
    curr_dir = os.getcwd()
    dir_above = curr_dir + "/downloaded_datasets"
    if overwrite:
        os.chdir(dir_above)
        os.remove(dataset_name)
        os.chdir(curr_dir)
    with open(dataset_name, "wb") as code:
        code.write(data.content)

def 
