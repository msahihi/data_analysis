import numpy as np
import matplotlib.pyplot as plt
from data_frame import DataFrame
from util import Util


exp1 = DataFrame('data/dataset_1/benchmark/')
exp1.get_time_series()
# exp1.visualize()

exp2 = DataFrame('data/dataset_2/benchmark/')
exp2.get_time_series()
# exp2.visualize()

util = Util()
dpoints = np.array([
    ['Group1', 'Category 1', exp1.data.Col1.mean()],
    ['Group2', 'Category 1', exp2.data.Col1.mean()],
    ['Group1', 'Category 2', util.percentile(exp1.data.Col1.values, 99)],
    ['Group2', 'Category 2', util.percentile(exp1.data.Col1.values, 99)],
    ['Group1', 'Category 3', exp1.data.Col1.min()],
    ['Group2', 'Category 3', exp2.data.Col1.min()],
    ['Group1', 'Category 4', exp1.data.Col1.max()],
    ['Group2', 'Category 4', exp2.data.Col1.max()],
    ['Group1', 'Category 5', exp1.data.Col1.var()],
    ['Group2', 'Category 5', exp2.data.Col1.var()],
])
util.bar_plot(221, dpoints, "1ts Comparision", y_label='Latency', x_label='Statistics parameters')
# plt.show()
util.bar_plot(222, dpoints, "2nd Comparision", y_label='Latency', x_label='Statistics parameters')
# plt.savefig('plot/{}.png'.format("FILENAME"))
plt.show()



