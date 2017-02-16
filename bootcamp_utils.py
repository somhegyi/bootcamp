import numpy as np

"""
This module contains functions written in the Caltech Python Bootcamp course.
"""

def ecdf(data):
    """
    Compute x, y values for an empirical distribution function.
    A histogram is a way of approximately representing the probability
    distribution function, or PDF, describing the data. The cumulative
    distribution function, or CDF, contains the same information as the PDF.
    It's just its integral. Importantly, we can plot the data to show what
    the CDF looks like, the so-called empirical cumulative distribution
    function, or ECDF, without the binning bias inherent in histograms.
    """
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y
