#!/usr/bin/env python2.7

import collections
import itertools

from matplotlib import pyplot
import numpy
from scipy.stats import norm


SAMPLE_SIZE = 1000
N = norm()


OrgStats = collections.namedtuple(
    "OrgStats", "accuracy bias acceptance_rate mean_quality_percentile")


def org_stats(accuracy, bias):
    cov = [[1., accuracy], [accuracy, 1.]]
    outcomes = numpy.random.multivariate_normal([0., 0.], cov, SAMPLE_SIZE)
    hired = outcomes[outcomes[:, 1] > N.ppf(bias), 0]
    mean_quality = hired.mean()
    return OrgStats(
        accuracy=accuracy,
        bias=bias,
        acceptance_rate=(hired.size / float(SAMPLE_SIZE)),
        mean_quality_percentile=N.cdf(hired.mean()))


domain = numpy.arange(0., 1. + numpy.spacing(1.), 0.01)
X, Y = numpy.meshgrid(
    domain,
    domain)


def contour(Z, levels):
    CS = pyplot.contour(X, Y, Z, levels=levels)
    pyplot.clabel(CS, inline=1, fontsize=10)
    pyplot.xlim(0., 1.)
    pyplot.ylim(0., 1.)
    pyplot.xlabel("accuracy")
    pyplot.ylabel("bias")
    pyplot.axes().set_aspect("equal")


Z = numpy.array([
    org_stats(x, y).mean_quality_percentile
    for x, y in zip(X.ravel(), Y.ravel())]).reshape(X.shape)
pyplot.title("The affect of bias and accuracy on mean employee quality.", y=1.05)
levels = numpy.arange(0.5, 1. + numpy.spacing(1.), 0.05)
contour(Z, levels)
pyplot.savefig("quality.png")
