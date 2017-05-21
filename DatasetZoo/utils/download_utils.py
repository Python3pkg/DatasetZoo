#!/usr/bin/env python
# -*- coding: utf-8 -*-


def __download_file(dataset_name, path_to_dataset, source=None,
        login_details=None, overwrite=False):
    """Download the dataset_name from source, and save it to path_to_dataset

    Args:
        dataset_name (str): name of the dataset to download. Must be valid and
        exist on the remote repo. For debugging purposes: must include .cdt but
        our __fix_name function in dzoo_client should handle it

        path_to_dataset (str): valid local path to store all the data to

    Kwargs:
        source (string):valid URL containing the dataset

        login_details (json): not implemented yet. Should interface with boto
        amazon plugin if the dataset is still stored on S3

        overwrite (bool): whether to overwrite any local datasets if conflicts.

    Returns:
        (data): non-fixed data type

    """
    import requests
    import sys
    from clint.textui import progress

    #########################################################
    # Handling the user input for what to do with the files #
    #########################################################
    if source is None:
        base = "https://s3.us-east-2.amazonaws.com/datasetzoo/datasets/"
    else:
        base = source  # The user has specified own dataset source
    data_src = base + dataset_name
    print("\nDownloading dataset. Might take a while\n")
    ######################################################
    # Actually downloading the file. Done using requests #
    ######################################################
    try:
        data = requests.get(data_src, stream=True)
    except:
        print(("Could not download dataset {0} from {1}. \
        Error message: {2} ".format(dataset_name, base)))
        sys.exit(1)

    with open(path_to_dataset + dataset_name, 'w') as f:
        total_length = int(data.headers.get('content-length'))
        for chunk in progress.bar(
                data.iter_content(chunk_size=1024),
                expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
    return data


def __dataset_exists(dataset_name, overwrite, dataset_dir):
    """Returns whether the dataset_name exists locally in dataset_dir

    Args:
        dataset_name (string): name of dataset to be downloaded. Must contain a
        .cdt

        overwrite (string): whether to overwrite if local one exists

        dataset_dir (string): valid local path

    Returns:
        (bool) whether the dataset exists locally

    """
    import os
    if dataset_name in os.listdir(dataset_dir):
        if overwrite:
            return False
        else:
            return True
    else:
        return False
