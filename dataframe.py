import os
import pandas as pd


class DataFrame(object):

    def __init__(self, path, features):
        super(DataFrame, self).__init__()
        self.path = path
        self.data = ''
        self.features = features

    def list_files(self, path, features=None):
        files_list = os.listdir(path)
        files_list = {file: path + file for file in files_list if file in features}
        return files_list

    def filter_files_by_feature(self, files_list, features):
        filtered_list = {}
        for file_name, file_path in files_list.items():
            feature = file_name.split('.')[0]
            if feature in features:
                filtered_list[file_name] = file_path
        return filtered_list

    def read_data_frame(self, file_name):
        data_frame = pd.read_csv(file_name, index_col=0, parse_dates=True)
        column_name_with_postfix = file_name.split('/')[-1]
        column_name = column_name_with_postfix.split('.')[0]
        column_value = {'value': column_name}
        data_frame.rename(columns=column_value, inplace=True)
        return data_frame

    def merge_data_frames(self, data_from_list):
        all_series = []
        item = 0
        for data_frame in data_from_list:
            item += 1
            data_frame.drop(data_frame.columns[0:1], axis=1, inplace=True)
            all_series.append(data_frame)
        merged_dataframe = pd.concat(all_series, axis=1)
        merged_dataframe.dropna(inplace=True)
        return merged_dataframe

    def merge_data_into_timeseries(self):
        files = self.list_files(self.path, features=self.features)
        data_frame_list = []
        for name, path in files.items():
            raw_data = self.read_data_frame(path)
            data_frame_list.append(raw_data)
        self.data = self.merge_data_frames(data_frame_list)
