import matplotlib.pyplot as plt
import matplotlib.cm as cm
import operator as o
import numpy as np


class DataFrameVisulization(object):

    def comparision_plot(self, ax, dpoints, title, y_label, x_label):
        fig = plt.figure('Result Comparision')
        ax = fig.add_subplot(ax)
        conditions = [(c, np.mean(dpoints[dpoints[:, 0] == c][:, 2].astype(float)))
                      for c in np.unique(dpoints[:, 0])]
        categories = [(c, np.mean(dpoints[dpoints[:, 1] == c][:, 2].astype(float)))
                      for c in np.unique(dpoints[:, 1])]
        conditions = [c[0] for c in sorted(conditions, key=o.itemgetter(1))]
        categories = [c[0] for c in sorted(categories, key=o.itemgetter(1))]
        dpoints = np.array(
            sorted(dpoints, key=lambda x: categories.index(x[1])))
        space = 0.3
        n = len(conditions)
        width = (1 - space) / (len(conditions))
        for i, cond in enumerate(conditions):
            indeces = range(1, len(categories) + 1)
            vals = dpoints[dpoints[:, 0] == cond][:, 2].astype(np.float)
            pos = [j - (1 - space) / 2. + i * width for j in indeces]
            ax.bar(pos, vals, width=width, label=cond,
                   color=cm.Accent(float(i) / n))
        ax.set_xticks(indeces)
        ax.set_xticklabels(categories)
        plt.setp(plt.xticks()[1], rotation=45)
        plt.title(title)
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1], loc='upper left')

    def aggr_plot(self, data, y_label, x_label):

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(9, 6))
        # fig.suptitle(title, fontsize=16)
        xticklabels = [k for k in data.iterkeys()]
        data = [v for v in data.itervalues()]
        axes.boxplot(data, vert=True, patch_artist=True,
            showfliers=True, showmeans=True)
        axes.set_ylim(0)
        axes.set_xlabel(x_label)
        axes.set_ylabel(y_label)
        plt.setp(axes, xticks=[y + 1 for y in range(len(data))],
                 xticklabels=xticklabels)

    def data_plot(self, data, **options):
        # option sample: options = {'kind': 'line', 'subplots': 'True', 'title': 'test', }
        data.plot(**options)
