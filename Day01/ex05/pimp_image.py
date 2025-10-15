from numpy import array
from PIL import Image


def ft_invert(array) -> array:
    tarray = 255 - array.copy()
    Image.fromarray(tarray).show()
    return tarray


def ft_red(array) -> array:
    tarray = array.copy()
    tarray[..., 1] = 0
    tarray[..., 2] = 0
    Image.fromarray(tarray).show()
    return tarray


def ft_green(array) -> array:
    tarray = array.copy()
    tarray[..., 0] = 0
    tarray[..., 2] = 0
    Image.fromarray(tarray).show()
    return tarray


def ft_blue(array) -> array:
    tarray = array.copy()
    tarray[..., 0] = 0
    tarray[..., 1] = 0
    Image.fromarray(tarray).show()
    return tarray


def ft_grey(array) -> array:
    tarray = array.copy()
    # Using only = and / operators
    grey = array.mean(axis=-1)
    tarray[..., 0] = grey
    tarray[..., 1] = grey
    tarray[..., 2] = grey
    Image.fromarray(tarray).show()
    return tarray
