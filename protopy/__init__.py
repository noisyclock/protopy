# author: Ma Tao
from .loader import Loader


def load(define, name):
    l = Loader()
    return l.load(define, name)


def load_from_file(fobj, name):
    l = loader()
    return l.load_file(fobj, name)



__all__ = (load, load_from_file)
