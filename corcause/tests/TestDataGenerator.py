import unittest
from corcause.src.DataGenerator import *


class DataGeneratorTest(unittest.TestCase):
    def test_uniform_distribution(self):
        distribution = uniform_distribution([4, 4, 4], 0.2)
        print(distribution)

    def test_correlated_distribution(self):
        cause = numpy.array(
            [[0.25, 0, 0, 0],
             [0.5, 0.5, 0, 0],
             [0.75, 0.75, 0.75, 0],
             [1, 1, 1, 1]]
        )
        effect = correlated_distribution(cause, 0.5, [1, 1])
        expected = numpy.array(
            [[0.5, 0.5, 0.5, 0.5],
             [0., 0.125, 0., 0.],
             [0., 0.25, 0.25, 0.],
             [0., 0.375, 0.375, 0.375]]
        )
        print(numpy.all(effect == expected))
        self.assertTrue(numpy.all(effect == expected), 'Expected:\n' + str(expected) + '\nGot:\n' + str(effect))


if __name__ == '__main__':
    unittest.main()
