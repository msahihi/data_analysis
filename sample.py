import matplotlib.pyplot as plt
import numpy as np
import logging

from visualization import DataFrameVisulization
from utils import StatisticUtil
from utils import Aggregation
from utils import Config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

statistic_util = StatisticUtil()
visualization = DataFrameVisulization()

cfg = Config('config_sample.yaml')
data, agg_filter = cfg.read_experiment_data()

aggr = Aggregation()
noop_aggr = aggr.aggregate(data['noop'], 'mean')
packing_aggr = aggr.aggregate(data['packing'], 'mean')
for column_name in agg_filter:
    noop_metric = getattr(noop_aggr, column_name)
    packing_metric = getattr(packing_aggr, column_name)
    s, p = statistic_util.t_test(noop_metric, packing_metric)
    logger.info('Metric: {}  Statistic: {}  P-Value: {}'.format(column_name, s, p))
    metrics = {
        'NOOP': noop_metric,
        'Packing': packing_metric
    }
    visualization.aggr_plot(metrics, column_name, 'Scheduler name')
# plt.show()
dpoints = np.array([
    ['NOOP', 'Mean',
        data['noop']['noop1'].data.cloudsuite_datacaching_99th.mean()],
    ['Packing', 'Mean',
     data['packing']['packing1'].data.cloudsuite_datacaching_99th.mean()],
    ['NOOP', '99th Aggr ',
     statistic_util.percentile(
         data['noop']['noop1'].data.cloudsuite_datacaching_99th.values, 99)],
    ['Packing', '99th Aggr ',
     statistic_util.percentile(
         data['packing']['packing1'].data.cloudsuite_datacaching_99th.values, 99)],
    ['NOOP', '99th Min',
     data['noop']['noop1'].data.cloudsuite_datacaching_99th.min()],
    ['Packing', '99th Min',
     data['packing']['packing1'].data.cloudsuite_datacaching_99th.min()],
    ['NOOP', '99th Max',
     data['noop']['noop1'].data.cloudsuite_datacaching_99th.max()],
    ['Packing', '99th Max',
     data['packing']['packing1'].data.cloudsuite_datacaching_99th.max()],
    ['NOOP', 'std',
     data['noop']['noop1'].data.cloudsuite_datacaching_99th.std()],
    ['Packing', 'std',
     data['packing']['packing1'].data.cloudsuite_datacaching_99th.std()],
])
cmp_title = '1ts Comparision'
y_label = 'Latency'
x_label = 'Statistics parameters'
visualization.comparision_plot(111, dpoints, cmp_title, y_label, x_label)
plt.show()
# # visualization.bar_plot(222, dpoints, "2nd Comparision", y_label, x_label)
# # plt.savefig('plot/{}.png'.format("FILENAME"))
