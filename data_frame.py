import os
import pandas as pd
import matplotlib.pyplot as plt


class DataFrame(object):
    """docstring for DataFrame"""

    def __init__(self, path):
        super(DataFrame, self).__init__()
        self.path = path
        self.data = ""

    def list_files(self, path, filter=None):
        files_list = os.listdir(path)
        files_list = {file: path + file for file in files_list}
        return files_list

    def read_data_frame(self, file):
        data_frame = pd.read_csv(file, index_col=0, parse_dates=True)
        return data_frame

    def merge_data_frames(self, data_from_list):
        all_series = []
        item = 0
        for data_frame in data_from_list:
            item += 1
            data_frame.rename(
                columns={'value': 'Col' + str(item)}, inplace=True)
            data_frame.drop(data_frame.columns[0:1], axis=1, inplace=True)
            all_series.append(data_frame)
        merged_dataframe = pd.concat(all_series, axis=1)
        merged_dataframe.dropna(inplace=True)
        return merged_dataframe

    def get_time_series(self):
        files = self.list_files(self.path)
        data_frame_list = []
        for name, path in files.items():
            raw_data = self.read_data_frame(path)
            data_frame_list.append(raw_data)
        self.data = self.merge_data_frames(data_frame_list)

    def visualize(self, **options):
        '''
        options refers to : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
        option sample: options = {'kind': 'line', 'subplots': 'True', 'title': 'test', }

        '''
        data = self.data
        data.plot(**options)
        plt.show()


