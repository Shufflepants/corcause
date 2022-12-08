import matplotlib.pyplot as plt
import numpy

from corcause.src import ClassifiedFeature


def plot3d(classified_feature: ClassifiedFeature):
    if classified_feature.domain.__len__() == 2:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x, y = numpy.meshgrid(numpy.linspace(*classified_feature.domain[0], classified_feature.data.shape[0]),
                              numpy.linspace(*classified_feature.domain[1], classified_feature.data.shape[1]))
        ax.scatter(x, y, classified_feature.data, c=classified_feature.data, cmap='jet')
    else:
        raise ValueError("plot may only be called on 3D feature")
