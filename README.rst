# Dataset Zoo

## Synopsis

The main idea of this projecet is to provide a lightweight system that enables researchers to download datasets via the use of a simple, dependency light system. Also, this project aims to meet the goal of allowing researchers to easily share their projects with the rest of the community: simply use the Dataset_zoo.dataset_upload function to store it on our servers (HDF5 only please, you can use the from_pkl_convert() function to convert from a pkl file to HDF5)

## Code Example

```
import Dataset_zoo as dz
```

List the datasets at the host site
```
dz.list_datasets(<host site>)
```

Download a dataset from host site
```
dz.download(<dataset_name>, <host site>)
```                         

List the locally installed datasets
```
dz.list_local_datasets(<dataset_name>)
```

Use a locally loaded dataset
```
dz.load_dataset(<downloaded dataset>)
```

## Motivation

Make it easier for researchers to download different datasets and integrate it into experiments by standardizing the format of all datasets, and providing an easy platform for institutions to share data both internally, and with the rest of the world

## Installation

```
pip install Dataset_zoo
```

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Built With

* Dropwizard - Bla bla bla
* Maven - Maybe
* Atom - ergaerga

## Contributing

Currently I'm very new to this process but do submit pull requests!

## Authors

* **Ian Quah**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details

## Acknowledgments

* My research advisor Amirali who encouraged me to pursue this
