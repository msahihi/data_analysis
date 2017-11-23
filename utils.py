from tdigest import TDigest
import pandas as pd


class StatisticUtil(object):
    """docstring for StatisticUtil"""

    def __init__(self):
        super(StatisticUtil, self).__init__()

    def percentile(self, data, percentage):
        digest = TDigest()
        digest.batch_update(data)
        return digest.percentile(percentage)


class Aggregation(object):
    """docstring for Aggregation"""

    def __init__(self):
        super(Aggregation, self).__init__()

    def get_index(self, data):
        index = []
        for key, data_frame in data.iteritems():
            index.append(key)
        return index

    def aggregate(self, data, method_name):
        index = self.get_index(data)
        df = pd.DataFrame(index=index)
        for key, data_frame in data.iteritems():
            for column in data_frame.columns.values:
                method = getattr(data_frame[column], method_name)
                df.set_value(key, column, method())

        return df
