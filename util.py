import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np


def bar(left, height, names, color, width, tick_num, rotation):
    """  bar plot

    Parameters
    ---------------
    left : left coordinates
    height : heights of the bar
    names : names for each bar
    color : color
    width : width of bar
    tick_num : number of xticks. xticks are evenly distributed.
    rotation : rotation of the xtick_labels

    Returns
    --------------
    None
    """
    N = len(left)
    # dur = left[-1] - left[0]
    plt.bar(left, height, color='r', width=width)
    if tick_num is not None:
        ticks = [names[pos] for pos in
                 range(0, N, N // tick_num)]
        # tick_pos = np.arange(left[0], left[-1], int(dur / tick_num))
        tick_pos = left[range(0, N, int(N / tick_num))]
        plt.xticks(tick_pos + width / 2., ticks, rotation=rotation)
    else:
        plt.xticks(np.array(left) + width / 2., names, rotation=rotation)


def stackplot(axes, x, y, legends, cmap=plt.cm.Spectral, xtick_labels=None,
              xtick_num=None, rotation=None, **kwargs):
    """Draws a stacked area plot.

    Parameters
    ----------------
    *x* : 1d array of dimension N

    *y* : 2d array of dimension MxN,
            stackplot(x, y)               # where y is MxN
    *cmap* : color map


    Returns
    --------------------
    *r* : A list of

    See Also
    ----------------------
    :class:`~matplotlib.collections.PolyCollection`, one for each
    element in the stacked area plot.
    """

    y = np.atleast_2d(y)
    M, N = y.shape
    # Assume data passed has not been 'stacked', so stack it here.
    y_stack = np.cumsum(y, axis=0)

    r = []

    # colors = np.linspace(0, 1, M)
    colors = np.random.random(size=M)

    # Color between x = 0 and the first array.
    r.append(axes.fill_between(x, 0, y_stack[0, :],
             facecolor=cmap(colors[0]), **kwargs))

    # Color between array i-1 and array i
    for i in xrange(len(y) - 1):
        r.append(axes.fill_between(x, y_stack[i, :], y_stack[i + 1, :],
                 facecolor=cmap(colors[i + 1]), **kwargs))

    fontP = FontProperties()
    fontP.set_size('small')
    # Add Legend
    pl = []
    for i in xrange(M):
        pl.append(plt.Rectangle((0, 0), 1, 1, facecolor=cmap(colors[i])))

    plt.legend(pl, legends, bbox_to_anchor=(0, 0, 1, 1),
               bbox_transform=plt.gcf().transFigure, prop=fontP)
    if xtick_num is not None:
        x = [x[i] for i in range(0, N, N/xtick_num)]
        xtick_labels = [xtick_labels[i] for i in range(0, N, N/xtick_num)]
    plt.xticks(x, xtick_labels, rotation=rotation)
    # plt.show()
    return r
