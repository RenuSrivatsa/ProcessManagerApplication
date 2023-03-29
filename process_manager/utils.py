import subprocess
import argparse
import sys
from constants import METRIC_DATA_INDEX_TUPLE

def get_process_metric(line_data):
    data_list = [d for d in line_data.split(' ') if d]
    data_length = len(data_list)
    data_dict = {}
    for i in range(data_length):
        if data_list[i]:
            data_dict[METRIC_DATA_INDEX_TUPLE[i][1]]=data_list[i]
    # print(data_dict)
    return data_dict
    


