import numpy
import scipy.signal


def a_given_b(a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
    return scipy.signal.correlate(a, b, 'full', 'auto') / numpy.sum(b)


def toroidal_a_given_b(a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
    tiled_b = numpy.tile(b, numpy.ones(b.ndim, int) * 3)
    return scipy.signal.correlate(a, tiled_b, 'same', 'auto') / numpy.sum(b)

