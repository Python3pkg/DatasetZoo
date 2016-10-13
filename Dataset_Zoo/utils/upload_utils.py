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


def already_exists():
    # check to see if a dataset of the same name
    # already exists, and if it does, reject it

    # could make it so that it sends an email to the
    # hosts, and notifies them that someone wants to upload
    # a dataset
    pass


def pkl_to_hdf5():
    # Look up how pkls work again,
    # enforce some sort of order and then just
    # create subgroups and such
    pass
