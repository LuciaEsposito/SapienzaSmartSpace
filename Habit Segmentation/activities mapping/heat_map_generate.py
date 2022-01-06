import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A list or array of two color specifications.  The first is used for
        values below a threshold, the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    #if threshold is not None:
    #    threshold = im.norm(threshold)
    #else:
    #    threshold = im.norm(data.max())/2.
    threshold = 40

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


activities = {'Bed_to_Toilet': [0, 4, 10, 2, 1, 4, 3, 2, 1, 1, 3, 5, 5, 3, 12, 9, 10, 10, 12, 8, 12, 9, 13, 13, 9, 3, 1, 3, 3, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 2, 2], 'Eating': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 4, 7, 5, 6, 11, 7, 6, 2, 5, 18, 15, 19, 20, 21, 10, 8, 5, 6, 4, 4, 9, 5, 7, 5, 3, 3, 6, 9, 9, 5, 4, 3, 4, 3, 5, 7, 3, 3, 4, 8, 7, 7, 5, 2, 10, 16, 15, 12, 7, 9, 11, 8, 4, 7, 6, 4, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0], 'Enter_Home': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 1, 3, 4, 1, 2, 2, 4, 5, 5, 3, 8, 7, 5, 10, 16, 14, 11, 12, 10, 5, 6, 4, 16, 23, 15, 18, 10, 16, 15, 36, 13, 6, 20, 7, 3, 8, 4, 7, 5, 6, 6, 8, 7, 9, 6, 5, 3, 3, 1, 2, 0, 1, 1, 0, 3, 0, 1, 1, 1, 0, 1, 2, 0, 0, 0], 'Housekeeping': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 2, 2, 4, 4, 5, 7, 5, 1, 0, 2, 2, 1, 1, 0, 0, 0, 1, 2, 4, 4, 4, 2, 2, 3, 2, 0, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Leave_Home': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 4, 8, 14, 15, 13, 10, 6, 3, 14, 6, 5, 8, 14, 9, 9, 17, 57, 11, 4, 6, 5, 5, 4, 6, 9, 8, 8, 10, 15, 24, 9, 4, 7, 10, 5, 6, 8, 8, 7, 5, 1, 5, 6, 9, 4, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Meal_Preparation': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 0, 2, 6, 2, 5, 20, 24, 15, 32, 37, 21, 28, 48, 45, 49, 56, 43, 50, 53, 48, 54, 49, 46, 55, 49, 44, 37, 27, 21, 25, 21, 27, 37, 32, 24, 19, 21, 31, 41, 33, 37, 35, 33, 23, 23, 33, 36, 30, 36, 31, 37, 46, 51, 58, 51, 62, 69, 63, 68, 66, 59, 53, 46, 29, 29, 21, 4, 4, 4, 3, 2, 4, 5, 0, 3, 0, 0, 1, 1, 0], 'Relax': [84, 47, 32, 22, 17, 14, 13, 8, 7, 5, 3, 2, 3, 3, 1, 1, 1, 1, 3, 7, 8, 16, 26, 38, 44, 65, 71, 59, 45, 52, 58, 68, 73, 83, 82, 98, 100, 95, 82, 76, 69, 67, 54, 60, 59, 55, 59, 51, 63, 69, 87, 81, 79, 90, 94, 102, 113, 115, 122, 127, 117, 116, 116, 126, 127, 134, 135, 141, 144, 140, 148, 150, 146, 164, 179, 183, 193, 206, 210, 225, 229, 230, 226, 224, 225, 226, 222, 212, 211, 192, 194, 172, 163, 147, 131, 109], 'Resperate': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Sleeping': [151, 178, 199, 202, 205, 207, 210, 210, 214, 215, 221, 219, 220, 220, 226, 224, 225, 224, 224, 217, 217, 203, 197, 188, 172, 150, 140, 130, 113, 101, 87, 74, 59, 45, 30, 17, 6, 5, 5, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 4, 3, 2, 1, 1, 1, 2, 3, 3, 3, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 2, 2, 2, 3, 4, 7, 10, 12, 14, 22, 31, 47, 57, 64, 82, 98, 118], 'Wash_Dishes': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 5, 2, 1, 6, 3, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 3, 4, 1, 3, 2, 2, 3, 3, 6, 5, 3, 1, 2, 5, 2, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0], 'Work': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 3, 3, 5, 5, 3, 5, 3, 4, 3, 6, 6, 6, 6, 3, 5, 8, 7, 3, 4, 8, 6, 4, 6, 9, 9, 8, 8, 8, 3, 6, 6, 7, 10, 8, 5, 4, 8, 7, 13, 16, 13, 12, 7, 6, 8, 8, 8, 7, 4, 4, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 1]}

labels = sorted(activities.keys())

slots = ["00:00-00:15", "00:15-00:30", "00:30-00:45", "00:45-01:00", "01:00-01:15", "01:15-01:30", "01:30-01:45", "01:45-02:00",
         "02:00-02:15", "02:15-02:30", "02:30-02:45", "02:45-03:00", "03:00-03:15", "03:15-03:30", "03:30-03:45", "03:45-04:00",
         "04:00-04:15", "04:15-04:30", "04:30-04:45", "04:45-05:00", "05:00-05:15", "05:15-05:30", "05:30-05:45", "05:45-06:00",
         "06:00-06:15", "06:15-06:30", "06:30-06:45", "06:45-07:00", "07:00-07:15", "07:15-07:30", "07:30-07:45", "07:45-08:00",
         "08:00-08:15", "08:15-08:30", "08:30-08:45", "08:45-09:00", "09:00-09:15", "09:15-09:30", "09:30-09:45", "09:45-10:00",
         "10:00-10:15", "10:15-10:30", "10:30-10:45", "10:45-11:00", "11:00-11:15", "11:15-11:30", "11:30-11:45", "11:45-12:00",
         "12:00-12:15", "12:15-12:30", "12:30-12:45", "12:45-13:00", "13:00-13:15", "13:15-13:30", "13:30-13:45", "13:45-14:00",
         "14:00-14:15", "14:15-14:30", "14:30-14:45", "14:45-15:00", "15:00-15:15", "15:15-15:30", "15:30-15:45", "15:45-16:00",
         "16:00-16:15", "16:15-16:30", "16:30-16:45", "16:45-17:00", "17:00-17:15", "17:15-17:30", "17:30-17:45", "17:45-18:00",
         "18:00-18:15", "18:15-18:30", "18:30-18:45", "18:45-19:00", "19:00-19:15", "19:15-19:30", "19:30-19:45", "19:45-20:00",
         "20:00-20:15", "20:15-20:30", "20:30-20:45", "20:45-21:00", "21:00-21:15", "21:15-21:30", "21:30-21:45", "21:45-22:00",
         "22:00-22:15", "22:15-22:30", "22:30-22:45", "22:45-23:00", "23:00-23:15", "23:15-23:30", "23:30-23:45", "23:45-00:00"]


values = np.array([activities["Bed_to_Toilet"],
                   activities["Eating"],
                   activities["Enter_Home"],
                   activities["Housekeeping"],
                   activities["Leave_Home"],
                   activities["Meal_Preparation"],
                   activities["Relax"],
                   activities["Resperate"],
                   activities["Sleeping"],
                   activities["Wash_Dishes"],
                   activities["Work"]])


fig, ax = plt.subplots()

im, cbar = heatmap(values, labels, slots, ax=ax,
                   cmap="YlGn", cbarlabel="n°occurrences")
texts = annotate_heatmap(im, valfmt="{x:d}", threshold=50)



fig = matplotlib.pyplot.gcf()
fig.set_size_inches(130, 20)
fig.savefig('heat_map_activities.jpg', quality=95)
