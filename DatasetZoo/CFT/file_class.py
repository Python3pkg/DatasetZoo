import json
import types
import sys
import numpy as np
try:
    from io import StringIO
except:
    from io import StringIO


class CFT(object):

    """A custom wrapper around the different data formats that we encounter
    during transferring datasets. Note that this just abstracts the different
    types of files, it doesn't serve as an optimized filetype
    """
    def __check_extension(self, filename):
        """Formats input filenames to be what we need

        Args:
            filename (string): file name

        Returns:
            (string): formatted filename
        """
        if filename[-4::] == ".cft":
            filename = filename[:-4]
        return (filename + ".cft")

    def __init__(self, filename, data=None):
        """Initialize things?

        Args:
            filename (string): filename to write to

        Kwargs:
            data (?): Data to be written. Non-fixed filetype

        """
        self._filename = filename
        self._data = data
        self.data = data
        self.__initialized = False
        self.__index = {}
        self.OFFSET_LENGTH = 12
        self.filename = self.__check_extension(filename)

    def __datum_write(self, datum, f):
        """Write individual "information chunk". Useful if a dataset contains
        multiple formats. E.g: VQA contains data in both images, and json which
        can't be stored easily as one file

        Args:
            datum (?): individual piece of data that was passed in to be
            written to a file

            f (string): where to write the data to

        """
        start = f.tell()
        inst_type = None
        if str(type(datum[1])).find("numpy") != -1:
            from .N_encoder import NumpyEncoder
            json.dump(datum[1], f, cls=NumpyEncoder)
            inst_type = "numpy"
        elif isinstance(datum[1], bytes):
            f.write(datum[1])
            inst_type = "string"
        elif isinstance(datum[1], dict):
            json.dump(datum[1], f)
            inst_type = "dict"
        elif isinstance(datum[1], int):
            f.write(str(datum[1]))
            inst_type = "int"
        elif isinstance(datum[1], list):
            f.write(str(datum[1]))
            inst_type = "list"
        else:
            try:
                print((type(datum), "is currently not explicitly supported" +
                      ". Contact the maintainer if there are any issues"))
                f.write(datum[1])
            except:
                print(("There was an error trying to write type: " +
                      type(datum) +
                      ". Please create an issue on github"))
                raise

        self.__index[datum[0]] = (start, f.tell() - start, inst_type)

    def write(self):
        """Writes the data to the file specified on the cdt creation

        Returns:
            None

        """
        f = open(self.filename, "w")
        data = self.data
        # error checking
        assert hasattr(data, '__iter__'), "Type data must be an iterable"
        if self.__initialized is False:
            f.write(self.filename)
            self.__initialized = True

        # Actual saving
        for datum in data:
            assert hasattr(datum, '__iter__'), \
                "individual elements of data must be iterable"
            assert (len(datum) == 2), "elements of data, must have length 2,\
            where the first element is the name, and the second is the data"
            self.__datum_write(datum, f)

        index_offset = f.tell()
        json.dump(self.__index, f)
        f.write(str(index_offset).zfill(self.OFFSET_LENGTH))
        f.close()

    def read(self, key):
        """Read the keys available from the file

        Args:
            key (string): valid key in the that exists in list_keys' output

        Returns:
            None

        """
        try:
            f = open(self.filename)
        except:
            print("File doesn't exist")
            sys.exit(1)

        # Finding the index offset
        f.seek(-1 * (self.OFFSET_LENGTH), 2)
        index_offset = int(f.read())
        f.seek(index_offset)
        boundary = f.read()[: -1 * self.OFFSET_LENGTH]
        ind = json.loads(boundary)

        # Getting the details of the key of interest
        start, length, inst_type = ind[key]
        f.seek(start)
        fo = StringIO(f.read(length))
        f.close()
        if inst_type == "numpy":
            from .N_encoder import json_numpy_obj_hook
            return np.asarray(json.load(fo, object_hook=json_numpy_obj_hook))
        elif inst_type == "dict":
            return json.load(fo)
        elif inst_type == "string":
            return (fo.read())
        elif inst_type == "int":
            return (int(fo.read()))

    def list_keys(self):
        """Lists all the keys that are within self.filename

        Returns:
            List: all the keys contained in the file

        """
        try:
            f = open(self.filename)
        except:
            print("File doesn't exist")
            sys.exit(1)

        # Finding the index offset
        f.seek(-1 * (self.OFFSET_LENGTH), 2)
        index_offset = int(f.read())
        f.seek(index_offset)
        index_ = json.loads(f.read()[: -1 * self.OFFSET_LENGTH])

        print((list(index_.keys())))
        return(list(index_.keys()))
