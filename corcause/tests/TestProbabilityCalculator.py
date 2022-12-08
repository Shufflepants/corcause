import unittest
from corcause.src.ProbabilityCalculator import *
import matplotlib.pyplot as plt


class ProbabilityCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.display = True

    def test_a_given_b(self):
        size = 5
        b = numpy.zeros([size, size])
        b[1, 1] = 1
        b[3, 3] = 1
        b[0, 2] = 1

        a = numpy.zeros([size, size])
        a[2, 2] = 1
        a[4, 4] = 1
        a[1, 3] = 1

        p_a_given_b = a_given_b(a, b)

        if self.display:
            print(p_a_given_b)
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            x, y = numpy.meshgrid(range(9), range(9))
            ax.scatter(x, y, p_a_given_b, c=p_a_given_b, cmap='jet')
            plt.show()

        self.assertEqual(p_a_given_b[5, 5], 1, 'Probability offset incorrect')

    def test_toroidal_a_given_b(self):
        size = 5
        b = numpy.zeros([size, size])
        b[1, 1] = 1
        b[3, 3] = 1
        b[0, 2] = 1

        a = numpy.zeros([size, size])
        a[2, 2] = 1
        a[4, 4] = 1
        a[1, 3] = 1

        toroidal_p_a_given_b = toroidal_a_given_b(a, b)

        if self.display:
            print(toroidal_p_a_given_b)
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            x, y = numpy.meshgrid(range(5), range(5))
            ax.scatter(x, y, toroidal_p_a_given_b, c=toroidal_p_a_given_b, cmap='jet')
            plt.show()

        self.assertEqual(toroidal_p_a_given_b[3, 3], 1, 'Probability offset incorrect')


if __name__ == '__main__':
    unittest.main()
