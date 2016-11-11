import numpy as np
import json
import types
import sys
try:
    from StringIO import StringIO
except:
    from io import StringIO


class CDT(object):
    """
    Functions to allow us to interact with a CDT file: a
    custom data type. Acts as a wrapper on a file
    """

    def __init__(self, filename, data=None):
        self.data = data
        self.filename = filename
        self.__initialized = False
        self.__index = {}
        self.OFFSET_LENGTH = 20

    def __datum_write(self, datum, f):
        start = f.tell()
        inst_type = None
        if str(type(datum[1])).find("numpy") != -1:
            print("Please note that only .npy files can be saved. .npz files\
             cannot be saved as we have disabled pickling")
            np.save(f, np.asarray(datum[1]), allow_pickle=False)
            inst_type = "numpy"
        elif isinstance(datum[1], types.StringType):
            f.write(datum[1])
            inst_type = "string"
        elif isinstance(datum[1], types.DictionaryType):
            json.dump(datum[1], f)
            inst_type = "dict"
        elif isinstance(datum[1], types.IntType):
            f.write(str(datum[1]))
            inst_type = "int"
        elif isinstance(datum[1], types.ListType):
            f.write(str(datum[1]))
            inst_type = "list"
        else:
            try:
                print(type(datum), "is currently not explicitly supported" +
                      ". Contact the maintainer if there are any issues")
                f.write(datum[1])
            except:
                print("There was an error trying to write type: ", type(datum),
                      "Please create an issue on github")
                raise

        self.__index[datum[0]] = (start, f.tell() - start, inst_type)

    def write(self):
        f = open(self.filename + ".cdt", "w")
        data = self.data
        # error checking
        assert hasattr(data, '__iter__'), "Type data must be an iterable"
        if self.__initialized is False:
            f.write(self.filename + str(self.__version))
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

    def modify(self):
        print("Modify is not implemented yet")
        pass

    def read(self, key):
        try:
            f = open(self.filename + ".cdt")
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
            return (np.load(fo))
        elif inst_type == "dict":
            return json.load(fo)
        elif inst_type == "string":
            return (fo.read())
        elif inst_type == "int":
            return (int(fo.read()))

    def list_keys(self):
        try:
            f = open(self.filename + ".cdt")
        except:
            print("File doesn't exist")
            sys.exit(1)

        # Finding the index offset
        f.seek(-1 * (self.OFFSET_LENGTH), 2)
        index_offset = int(f.read())
        f.seek(index_offset)
        index = json.loads(f.read()[: -1 * self.OFFSET_LENGTH])

        print(index.keys())
        return(index.keys())
