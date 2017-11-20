import os
import pandas as pd
import matplotlib.pyplot as plt


class DataFrame(object):
    """docstring for DataFrame"""

    def __init__(self, path):
        super(DataFrame, self).__init__()
        self.path = path
        self.data = ''
        self.filter_set = ''

    def list_files(self, path, filter_set=None):
        files_list = os.listdir(path)
        files_list = {file: path + file for file in files_list if file not in filter_set}
        return files_list

    def set_filter(self, filter_set):
        self.filter_set = filter_set

    def filter_files(self, files_list, filter_set):
        output_list = {}
        for file_name, file_path in files_list.items():
            feature = file_name.split('.')[0]
            if feature in filter_set:
                output_list[file_name] = file_path
        return output_list

    def read_data_frame(self, file):
        data_frame = pd.read_csv(file, index_col=0, parse_dates=True)
        column_name_with_postfix = file.split('/')[-1]
        column_name = column_name_with_postfix.split('.')[0]
        data_frame.rename(
                columns={'value': column_name}, inplace=True)
        return data_frame

    def merge_data_frames(self, data_from_list):
        all_series = []
        item = 0
        for data_frame in data_from_list:
            item += 1
            data_frame.drop(data_frame.columns[0:1], axis=1, inplace=True)
            all_series.append(data_frame)
        merged_dataframe = pd.concat(all_series, axis = 1)
        merged_dataframe.dropna(inplace=True)
        return merged_dataframe

    def get_time_series(self):
        files = self.list_files(self.path, filter_set= self.filter_set)
        data_frame_list = []
        for name, path in files.items():
            raw_data = self.read_data_frame(path)
            data_frame_list.append(raw_data)
        self.data = self.merge_data_frames(data_frame_list)




