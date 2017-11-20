import matplotlib.pyplot as plt
import matplotlib.cm as cm
import operator as o
import numpy as np


class DataFrameVisulization(object):
    """docstring for DataFrameVisulization"""

    def __init__(self):
        super(DataFrameVisulization, self).__init__()

    def comparision_plot(self, ax, dpoints, title, y_label, x_label):
        # based on http://emptypipes.org/2013/11/09/matplotlib-multicategory-barchart/
        '''
        Create a barchart for data across different categories with
        multiple conditions for each category.

        @param ax: The plotting axes from matplotlib.
        @param dpoints: The data set as an (n, 3) numpy array
        '''

        # Aggregate the conditions and the categories according to their
        # mean values
        fig = plt.figure("Result Comparision")
        ax = fig.add_subplot(ax)
        conditions = [(c, np.mean(dpoints[dpoints[:, 0] == c][:, 2].astype(float)))
                      for c in np.unique(dpoints[:, 0])]
        categories = [(c, np.mean(dpoints[dpoints[:, 1] == c][:, 2].astype(float)))
                      for c in np.unique(dpoints[:, 1])]

        # sort the conditions, categories and data so that the bars in
        # the plot will be ordered by category and condition
        conditions = [c[0] for c in sorted(conditions, key=o.itemgetter(1))]
        categories = [c[0] for c in sorted(categories, key=o.itemgetter(1))]

        dpoints = np.array(
            sorted(dpoints, key=lambda x: categories.index(x[1])))

        # the space between each set of bars
        space = 0.3
        n = len(conditions)
        width = (1 - space) / (len(conditions))

        # Create a set of bars at each position
        for i, cond in enumerate(conditions):
            indeces = range(1, len(categories) + 1)
            vals = dpoints[dpoints[:, 0] == cond][:, 2].astype(np.float)
            pos = [j - (1 - space) / 2. + i * width for j in indeces]
            ax.bar(pos, vals, width=width, label=cond,
                   color=cm.Accent(float(i) / n))

        # Set the x-axis tick labels to be equal to the categories
        ax.set_xticks(indeces)
        ax.set_xticklabels(categories)
        plt.setp(plt.xticks()[1], rotation=45)
        plt.title(title)

        # Add the axis labels
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)

        # Add a legend
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1], loc='upper left')

    def data_plot(self, data, **options):
        '''
        options refers to : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
        option sample: options = {'kind': 'line', 'subplots': 'True', 'title': 'test', }

        '''
        data.plot(**options)

