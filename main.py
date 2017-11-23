import numpy as np
import matplotlib.pyplot as plt
from data_frame import DataFrame

from visualization import DataFrameVisulization
from utils import StatisticUtil
from utils import Aggregation

statistic_util = StatisticUtil()
visualization = DataFrameVisulization()

'''
Creating filter to specify the files need to be read in each directory
'''
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
'''
Reading files from a directory and filtering them by file_filter variable
'''
exp1 = DataFrame('data/dataset_1/benchmark/')
exp1.set_filter(file_filter)
exp1.get_time_series()
options = {'kind': 'line', 'title': 'Experiment 1', }
visualization.data_plot(exp1.data, **options)

exp2 = DataFrame('data/dataset_2/benchmark/')
exp2.set_filter(file_filter)
exp2.get_time_series()

exp3 = DataFrame('data/dataset_3/benchmark/')
exp3.set_filter(file_filter)
exp3.get_time_series()

exp4 = DataFrame('data/dataset_4/benchmark/')
exp4.set_filter(file_filter)
exp4.get_time_series()

exp5 = DataFrame('data/dataset_5/benchmark/')
exp5.set_filter(file_filter)
exp5.get_time_series()

exp6 = DataFrame('data/dataset_6/benchmark/')
exp6.set_filter(file_filter)
exp6.get_time_series()


'''
Aggreate all experiment into two different group
'''
cat1 = {
    'Experiment1': exp1.data,
    'Experiment2': exp2.data,
    'Experiment3': exp3.data,
}

cat2 = {
    'Experiment4': exp4.data,
    'Experiment5': exp5.data,
    'Experiment6': exp6.data
}

aggr = Aggregation()
cat1_aggr = aggr.aggregate(cat1, 'mean')
cat2_aggr = aggr.aggregate(cat2, 'mean')
columns = [
    'cloudsuite_datacaching_90th',
    'cloudsuite_datacaching_99th'
]

for column_name in columns:
    data = {
        'cat1': getattr(cat1_aggr, column_name),
        'cat2': getattr(cat2_aggr, column_name)
    }
    visualization.aggr_plot(data, column_name, 'Y label')


'''
Comparing experiments grouped by their metrics
'''
dpoints = np.array([
    ['experimnet1', 'Mean', exp1.data.cloudsuite_datacaching_99th.mean()],
    ['experiment2', 'Mean', exp2.data.cloudsuite_datacaching_99th.mean()],
    ['experimnet1', '99th Aggr ', statistic_util.percentile(
        exp1.data.cloudsuite_datacaching_99th.values, 99)],
    ['experiment2', '99th Aggr ', statistic_util.percentile(
        exp1.data.cloudsuite_datacaching_99th.values, 99)],
    ['experimnet1', '99th Min', exp1.data.cloudsuite_datacaching_99th.min()],
    ['experiment2', '99th Min', exp2.data.cloudsuite_datacaching_99th.min()],
    ['experimnet1', '99th Max', exp1.data.cloudsuite_datacaching_99th.max()],
    ['experiment2', '99th Max', exp2.data.cloudsuite_datacaching_99th.max()],
    ['experimnet1', 'std', exp1.data.cloudsuite_datacaching_99th.std()],
    ['experiment2', 'std', exp2.data.cloudsuite_datacaching_99th.std()],
    # ['experimnet1', 'Variance', exp1.data.gwdg_cloudsuite_datacaching_99th.var()],
    # ['experiment2', 'Variance', exp2.data.gwdg_cloudsuite_datacaching_99th.var()],
])
visualization.comparision_plot(
    111, dpoints, "1ts Comparision", y_label='Latency', x_label='Statistics parameters')
# util.bar_plot(222, dpoints, "2nd Comparision", y_label='Latency', x_label='Statistics parameters')
# plt.savefig('plot/{}.png'.format("FILENAME"))
plt.show()
