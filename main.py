import numpy as np
import matplotlib.pyplot as plt
from data_frame import DataFrame

from visualization import DataFrameVisulization
from utils import StatisticUtil


statistic_util = StatisticUtil()
visualization = DataFrameVisulization()
exp1 = DataFrame('data/dataset_1/benchmark/')
file_filter = [
    'cloudsuite_datacaching_95th.csv',
    'cloudsuite_datacaching_avg_lat.csv',
    'cloudsuite_datacaching_avgGetSize.csv',
    'cloudsuite_datacaching_gets.csv',
    'cloudsuite_datacaching_hits.csv',
    'cloudsuite_datacaching_max.csv',
    'cloudsuite_datacaching_min.csv',
    'cloudsuite_datacaching_misses.csv',
    'cloudsuite_datacaching_requests.csv',
    'cloudsuite_datacaching_sets.csv',
    'cloudsuite_datacaching_std.csv',
    'cloudsuite_datacaching_rps.csv',

]
exp1.set_filter(file_filter)
exp1.get_time_series()
options = {'kind': 'line', 'title': 'Experiment 1', }
visualization.data_plot(exp1.data, **options)

exp2 = DataFrame('data/dataset_2/benchmark/')
# exp2.set_filter(file_filter)
exp2.get_time_series()
# visualization.data_plot(exp2.data)


dpoints = np.array([
    ['Normal', 'Mean', exp1.data.cloudsuite_datacaching_99th.mean()],
    ['Packing', 'Mean', exp2.data.cloudsuite_datacaching_99th.mean()],
    ['Normal', '99th Aggr ', statistic_util.percentile(exp1.data.cloudsuite_datacaching_99th.values, 99)],
    ['Packing', '99th Aggr ', statistic_util.percentile(exp1.data.cloudsuite_datacaching_99th.values, 99)],
    ['Normal', '99th Min', exp1.data.cloudsuite_datacaching_99th.min()],
    ['Packing', '99th Min', exp2.data.cloudsuite_datacaching_99th.min()],
    ['Normal', '99th Max', exp1.data.cloudsuite_datacaching_99th.max()],
    ['Packing', '99th Max', exp2.data.cloudsuite_datacaching_99th.max()],
    ['Normal', 'std', exp1.data.cloudsuite_datacaching_99th.std()],
    ['Packing', 'std', exp2.data.cloudsuite_datacaching_99th.std()],
    # ['Normal', 'Variance', exp1.data.gwdg_cloudsuite_datacaching_99th.var()],
    # ['Packing', 'Variance', exp2.data.gwdg_cloudsuite_datacaching_99th.var()],
])
visualization.comparision_plot(111, dpoints, "1ts Comparision", y_label='Latency', x_label='Statistics parameters')
# util.bar_plot(222, dpoints, "2nd Comparision", y_label='Latency', x_label='Statistics parameters')
# plt.savefig('plot/{}.png'.format("FILENAME"))
plt.show()

