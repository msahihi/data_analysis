import yaml
import pandas as pd
from scipy import stats
from tdigest import TDigest

from dataframe import DataFrame


class Config(object):

    def __init__(self, file_name):
        super(Config, self).__init__()
        self.file_name = file_name

    def read_config_file(self):
        stream = open(self.file_name, "r")
        cfg = yaml.load(stream)
        return cfg['collection']

    def read_experiment_data(self):
        cfg = self.read_config_file()
        filter_list = cfg['filter_list']
        agg_filter = cfg['aggregation']
        columns_list = cfg['columns_list']
        base_path = cfg['base_path']
        data = {}
        for group, values in cfg['experiment'].items():
            if group not in data:
                data[group] = {}
            for experiment_name, exp_arg in values.items():
                experimen_path = cfg['experiment'][group][experiment_name]['path']
                data[group].update(
                    {experiment_name: DataFrame(base_path + experimen_path, filter_list)})
                data[group][experiment_name].merge_data_into_timeseries(columns_list)
        return data, agg_filter


class StatisticUtil(object):

    def percentile(self, data, percentage):
        digest = TDigest()
        digest.batch_update(data)
        return digest.percentile(percentage)

    def t_test(self, list_1, list_2, equal_var=False):
        return stats.ttest_ind(list_1, list_2)


class Aggregation(object):

    def get_index(self, data):
        index = []
        for key, data_frame in data.iteritems():
            index.append(key)
        return index

    def aggregate(self, data, column_filter, method_name):
        index = self.get_index(data)
        df = pd.DataFrame(index=index)
        for key, data_frame in data.iteritems():
            for column in column_filter:
                method = getattr(data_frame.data[column], method_name)
                df.set_value(key, column, method())

        return df
