# Dataset Zoo

## Synopsis

The technological advantage of this project is that it provides a lighweight interface, that works across multiple python versions.

From a research point of view, the less time you spend looking for datasets, and the less time you need to spend understanding how they work, the faster you can proceed with your work.

#### The upload functionality is not working as of now. If you have any suggestions on how to run a backend (some sort of server that can register users, keep track of permissions and such), do submit a pull request, or email me.

## Code Example


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

## Acknowledgments

* My research advisor [Amirali](http://www.amiralibagherzadeh.com/) who encouraged me to pursue this

* CMUs' [Language Technologies Institute](https://www.lti.cs.cmu.edu/) and more specifically [Professor Morency](https://www.cs.cmu.edu/~morency/) for funding the S3 instance that hosts our datasets.
