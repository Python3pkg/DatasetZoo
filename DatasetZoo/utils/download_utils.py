

def __download_file(dataset_name, path_to_dataset,
                    source=None, login_details=None,
                    overwrite=False):
    """Download the specified file

    :param dataset_name: string: name of dataset to download. Include .h5
    :param path_to_dataset: string: valid local path to save to
    :param source: string: valid url to download from
    :param login_details: dict : login details
    :param overwrite: bool
    :returns: dataset
    :rtype: h5 file

    """
    import requests
    import sys
    from clint.textui import progress
    import h5py

    #########################################################
    # Handling the user input for what to do with the files #
    #########################################################
    if source is None:
        base = "https://s3.amazonaws.com/datasetzoo/datasets/"
    else:
        base = source  # The user has specified own dataset source
    data = base + dataset_name
    print("\nDownloading dataset. Might take a while\n")

    ######################################################
    # Actually downloading the file. Done using requests #
    ######################################################
    try:
        data = requests.get(data, stream=True)
    except:
        print("Could not download dataset {0} from {1}. \
        Error message: {2} ".format(dataset_name, base))
        sys.exit(1)

    with open(path_to_dataset + dataset_name, 'w') as f:
        total_length = int(data.headers.get('content-length'))
        for chunk in progress.bar(
                data.iter_content(chunk_size=1024),
                expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
    data = h5py.File(path_to_dataset + dataset_name, "r")
    return data


def __dataset_exists(dataset_name, save, overwrite, dataset_dir):
    """ Returns whether dataset_name exists locally

    :param dataset_name: string: name of dataset to be downloaded, with .h5
    :param save: bool: whether to save
    :param overwrite: bool: whether to overwrite if local one exists
    :param dataset_dir: string: valid local path to check
    :returns: whether dataset_name exists locally
    :rtype: bool

    """
    import os
    dataset_name = dataset_name
    if dataset_name in os.listdir(dataset_dir):
        if overwrite:
            return False
        else:
            raise True
    else:
        return False
