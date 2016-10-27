def verify_type(dataset):
    """
    :p dataset: the dataset which we need to verify
    ;t dataset: file type, but should be h5py

    returns True or False
    """
    return (isinstance(dataset, "h5py._hl.files.File"))


def verify_information(dataset):
    """
    :p dataset: dataset to be accessed
    :t dataset: h5py

    verify that it follows the requirements
    1) description
    2) X's
    3) Y's
    4) Misc

    returns True if at the top level, there are all the above
    data
    """
    try:
        dataset["/description"]
        dataset["/X"]
        dataset["/Y"]
        dataset["/Misc"]
        return True
    except:
        print("Please follow the format laid out. The top level should have 4\
        keys: description, X, Y and Misc")
        return False


def _upload(name, dataset):
    pass
