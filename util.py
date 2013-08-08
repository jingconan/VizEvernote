import matplotlib.pyplot as plt
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
    dur = left[-1] - left[0]
    plt.bar(left, height, color='r', width=width)
    if tick_num is not None:
        ticks = [names[pos] for pos in
                 range(0, N, N // tick_num)]
        tick_pos = np.arange(left[0], left[-1], int(dur / tick_num))
        plt.xticks(tick_pos + width / 2., ticks, rotation=rotation)
    else:
        plt.xticks(np.array(left) + width / 2., names, rotation=rotation)


"""
Stacked area plot for 1D arrays inspired by Douglas Y'barbo's stackoverflow
answer:
http://stackoverflow.com/questions/2225995/how-can-i-create-stacked-line-graph-with-matplotlib

(http://stackoverflow.com/users/66549/doug)

"""
import numpy as np

__all__ = ['stackplot']


def stackplot(axes, x, *args, **kwargs):
    """Draws a stacked area plot.

    *x* : 1d array of dimension N

    *y* : 2d array of dimension MxN, OR any number 1d arrays each of dimension
          1xN. The data is assumed to be unstacked. Each of the following
          calls is legal::

            stackplot(x, y)               # where y is MxN
            stackplot(x, y1, y2, y3, y4)  # where y1, y2, y3, y4, are all 1xNm

    Keyword arguments:

    *colors* : A list or tuple of colors. These will be cycled through and
               used to colour the stacked areas.
               All other keyword arguments are passed to
               :func:`~matplotlib.Axes.fill_between`

    Returns *r* : A list of
    :class:`~matplotlib.collections.PolyCollection`, one for each
    element in the stacked area plot.
    """

    if len(args) == 1:
        y = np.atleast_2d(*args)
    elif len(args) > 1:
        y = np.row_stack(args)

    colors = kwargs.pop('colors', None)
    if colors is not None:
        axes.set_color_cycle(colors)

    # Assume data passed has not been 'stacked', so stack it here.
    y_stack = np.cumsum(y, axis=0)

    r = []

    # Color between x = 0 and the first array.
    r.append(axes.fill_between(x, 0, y_stack[0, :],
             facecolor=axes._get_lines.color_cycle.next(), **kwargs))

    # Color between array i-1 and array i
    for i in xrange(len(y) - 1):
        r.append(axes.fill_between(x, y_stack[i, :], y_stack[i + 1, :],
                 facecolor=axes._get_lines.color_cycle.next(), **kwargs))
    return r
