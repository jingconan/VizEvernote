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
