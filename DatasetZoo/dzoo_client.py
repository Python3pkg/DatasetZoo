# coding: utf-8
#!/usr/bin/env python


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

    :param dataset_name: string: name of dataset to download. Include .cdt
    :param save: bool: whether to save the data
    :param overwrite: bool: whether to overwrite if we find conflict
    :param source: string: valid url to download from
    :param login_details: dict : login details

    :returns: dataset
    :rtype: cdt instance

    returns a single CDT object which must have 4 top level groups
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
    if dataset_name[-4::] == ".cdt":
        dataset_name = dataset_name[:-4]
    if __dataset_exists(dataset_name, overwrite, dataset_dir):
        return load_dataset(dataset_name)
    else:
        data = __download_file(dataset_name, dataset_dir,
                               source, login_details, save)
        return data
    # ENDIF: should never hit here as we'll error out within download_utils


def load_dataset(dataset_name):
    """
    :p dataset cdt file, which we saved to disk
    :t dataset string name

    returns the dataset
    """
    import os.path
    from CFT.file_class import CDT
    curr_dir = os.path.dirname(__file__)
    dataset_dir = curr_dir + "/downloaded_datasets/"
    if dataset_name[-4::] == ".cdt":
        dataset_name = dataset_name[:-4]
    try:
        f = CDT(filename=dataset_name)
        f = open(dataset_dir + dataset_name, 'r')
        return f
    except:
        print("There was an error accessing the data. \n\
        Use list_installed_datasets to view what is installed locally\n\
        Else please download the appropriate dataset")
        return None


def list_remote_datasets(source=None):
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
        print("No datasets downloaded yet")
    else:
        for dataset in os.listdir(dataset_dir):
            if (".py" in dataset) or (".pyc" in dataset):
                continue
            else:
                print(dataset)
    return
