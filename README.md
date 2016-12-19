# Dataset Zoo

## Synopsis

The technological advantage of this project is that it provides a lighweight interface, that works across multiple python versions, and it enables you to package datasets in a safe way.

From a research point of view, the less time you spend looking for datasets, and the less time you need to spend understanding how they work, the faster you can proceed with your work.

#### The upload functionality is not working as of now. If you have any suggestions on how to run a backend (some sort of server that can register users, keep track of permissions and such), do submit a pull request, or email me.

## Code Example

from DatasetZoo.CFT.file_class import CFT

### Custom data tyoe


Creating a CFT instance
```

easy_data = CFT(filename="data.cft")

```
Writing with a CFT instance
```
my_data = some_list_of_lists  # first element is key, and the second is value, all wrapped up into a list within a larger list

easy_data = CFT(filename="data.cft", data=my_data)
easy_data.write()

```
Reading with a CFT instance
```

easy_data = CFT(filename="data.cft")
easy_data.list_keys()  # select one of them
easy_data.read("valid_key")
```

The data is loaded in lazily, and should avoid any serialization issues (precision issues + issues with
misshappen data). If there are any issues please open an issue on Github.

### Dataset Zoo itself


```
import DatasetZoo.dzoo_client as dz
```

List the datasets at the host site
```
dz.list_source_datasets(<host site>)
```

Download a dataset from source site
```
dz.download(<dataset_name>, source=<host site>)
```               

List all locally installed datasets
```
dz.list_local_datasets()
```

Use a locally loaded dataset
```
dz.load_dataset(<downloaded dataset>)
```

## Motivation

After burning hours into searching for datasets, only to spend more time having to understand how they worked, my research advisor suggested creating

1) a single site from which to download datasets

2) a uniform, easily understandable format to manage datasets

which led to many problems involving Pickling (questions of safety), and HDF5 (where it was hard to add datasets beyond just numpy arrays), and thus the CFT was born. CFT stands for custom file type, and it provides you with an interface to act on the dataset, calling different sections of the data as if they were all processed and loaded into a clean dictionary on your local machine

## Installation

```
pip install DatasetZoo
```

## Contributing

Currently I'm very new to this process but do submit pull requests!

## Authors

* **Ian Quah**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details

* My research advisor [Amirali](http://www.amiralibagherzadeh.com/) who encouraged me to pursue this
