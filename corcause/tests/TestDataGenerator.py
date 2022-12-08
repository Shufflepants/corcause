import unittest
from corcause.src.DataGenerator import *
import matplotlib.pyplot as plt
from corcause.src.Display import plot3d


class DataGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.display = True

    def test_uniform_distribution(self):
        distribution = uniform_distribution([4, 4, 4], 0.2)
        if self.display:
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
        if self.display:
            print(cause)
            print(effect)

        self.assertTrue(numpy.all(effect == expected), 'Expected:\n' + str(expected) + '\nGot:\n' + str(effect))

    def test_noisy_gaussian_correlate_distribution(self):
        size = 100
        domain = [(0, 100), (0, 50)]
        distribution = ClassifiedFeature(uniform_distribution([size, size], 0.001), domain)
        gaussian = ClassifiedFeature(noisy_gaussian_correlated_distribution(distribution, 5), domain)
        distribution_sum = float(numpy.sum(distribution.data))
        gaussian_sum = float(numpy.sum(gaussian.data))
        if self.display:
            print("Distribution sum: " + str(distribution_sum))
            print("Gaussian sum: " + str(gaussian_sum))
            plot3d(distribution)
            plot3d(gaussian)
            plt.show()

        self.assertAlmostEqual(distribution_sum, gaussian_sum)


if __name__ == '__main__':
    unittest.main()
