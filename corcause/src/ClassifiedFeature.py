import numpy
from typing import List


class ClassifiedFeature:
    def __init__(self, data: numpy.ndarray, domain: List[tuple]):
        """

        :param data: Multidimensional array containing the data.
        :param domain: A list of tuples containing the start and end of the domain of each dimension of the data array.
        """
        self.data = data
        self.domain = domain
