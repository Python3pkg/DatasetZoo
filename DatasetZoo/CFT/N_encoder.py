import base64
import json
import numpy as np


class NumpyEncoder(json.JSONEncoder):

    """Custom type for efficient handling of numpy arrays by using
    C_Contiguous"""

    def default(self, obj):
        """Converts obj, an ndarray to a dict recording the data, dtype,
        and base encoded

        Args:
            obj (np.ndarray): numpy array to be encoded

        Returns:
            Encoded item, or error

        """

        if isinstance(obj, np.ndarray) and obj.dim == 1:
            return obj.tolist()
        elif isinstance(obj, np.generic):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            if obj.flags['C_CONTIGUOUS']:
                obj_data = obj.data
            else:
                cont_obj = np.ascontiguousarray(obj)
                assert(cont_obj.flags['C_CONTIGUOUS'])
                obj_data = cont_obj.data
            data_b64 = base64.b64encode(obj_data)
            return dict(__ndarray__=data_b64,
                        dtype=str(obj.dtype),
                        shape=obj.shape)
        else:
            return json.JSONEncoder(self, obj)


def json_numpy_obj_hook(dct):
    """Decodes a previously encoded numpy ndarray with proper shape and dtype.

    :param dct: (dict) json encoded ndarray
    :return: (ndarray) if input was an encoded ndarray
    """
    if isinstance(dct, dict) and '__ndarray__' in dct:
        data = base64.b64decode(dct['__ndarray__'])
        return np.frombuffer(data, dct['dtype']).reshape(dct['shape'])
    return dct

"""
expected = np.arange(100, dtype=np.float)
dumped = json.dumps(expected, cls=NumpyEncoder)
result = json.loads(dumped, object_hook=json_numpy_obj_hook)
"""
