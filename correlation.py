#!/usr/bin/env python2.7

import collections
import itertools

from matplotlib import pyplot
import numpy


SAMPLE_SIZE = 100

def ellipse(accuracy):
    cov = [[1., accuracy], [accuracy, 1.]]
    return numpy.random.multivariate_normal([0., 0.], cov, SAMPLE_SIZE)

e = ellipse(0.)
pyplot.subplot(2, 2, 1)
pyplot.scatter(e[:, 0], e[:, 1])
pyplot.axis("equal")
pyplot.axis([-4,4,-4,4])
pyplot.title("p=0.0")

e = ellipse(.33)
pyplot.subplot(2, 2, 2)
pyplot.scatter(e[:, 0], e[:, 1])
pyplot.axis("equal")
pyplot.axis([-4,4,-4,4])
pyplot.title("p=0.33")

e = ellipse(.66)
pyplot.subplot(2, 2, 3)
pyplot.scatter(e[:, 0], e[:, 1])
pyplot.axis("equal")
pyplot.axis([-4,4,-4,4])
pyplot.title("p=0.66")

e = ellipse(1.)
pyplot.subplot(2, 2, 4)
pyplot.scatter(e[:, 0], e[:, 1])
pyplot.axis("equal")
pyplot.axis([-4,4,-4,4])
pyplot.title("p=1.0")

pyplot.suptitle("The affect of correlation.", y=1.05)

pyplot.savefig("correlation.png")
