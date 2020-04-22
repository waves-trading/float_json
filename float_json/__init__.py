""""""
__version__ = '0.0.1'

__all__ = [
    'dump', 'dumps', 'load', 'loads',
    'JSONDecoder', 'JSONDecodeError', 'JSONEncoder',
]

__author__ = 'Ivister <ashitik@web3tech.ru>'

from functools import wraps
from json import (
    dump as _dump,
    dumps as _dumps,
    load,
    loads,
    JSONDecoder,
    JSONDecodeError,
    JSONEncoder

)

from .encoder import FloatEncoder


def float_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "cls" not in kwargs:
            kwargs["cls"] = FloatEncoder
        return func(*args, **kwargs)

    return wrapper


dump = float_wrapper(_dump)
dumps = float_wrapper(_dumps)
