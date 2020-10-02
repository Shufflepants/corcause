import numpy
import random
from typing import List


def uniform_distribution(shape: List[int], probability) -> numpy.ndarray:
    """
    Returns an x_1 by x_2 by ... by x_n matrix with x_i's specified by the elements of shape
    The elements of distribution are randomly generated as 1's with a probability specified by probability; 0 otherwise
    :param shape:
    :param probability: Should be in the range 0 to 1 inclusive
    :return:
    """
    distribution = numpy.zeros(shape)
    for index, item in numpy.ndenumerate(distribution):
        if random.random() < probability:
            distribution[index] = 1
    return distribution


#
def correlated_distribution(cause: numpy.ndarray, probability, offset: List[int]) -> numpy.ndarray:
    effect = numpy.zeros(cause.shape)
    with numpy.nditer([cause, effect], ['multi_index'], [['readonly'], ['writeonly']]) as it:
        for c, e in it:
            index = numpy.add(it.multi_index, offset)
            it.operands[1].put(numpy.ravel_multi_index(index, cause.shape, 'wrap'), probability * c)
        return it.operands[1]
