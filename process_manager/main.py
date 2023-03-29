import subprocess
import argparse
import sys
import os
import re

PROCESS_METRICES_TITLES = 'PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND'
METRIC_DATA_INDEX_TUPLE = ((0,'PID'),
                           (1,'USER'),
                           (2,'PRIORITY'),
                           (3, 'NICE VALUE'),
                           (4, 'VIRTUAL'),
                           (5, 'RESERVED'),
                           (6,'SHARDED'),
                           (7,'STATUS'),
                           (8,'%CPU '),
                           (9,'%MEMORY'),
                           (10,'TIME'),
                           (11,'COMMAND'),
                           (12,'NONE'),
                           (13,'NONE'))


def get_process_metric(line_data):
    data_list = [d for d in line_data.split(' ') if d]
    data_length = len(data_list)-1
    return [{METRIC_DATA_INDEX_TUPLE[i][1]:data_list[i]} for i in range(data_length) if data_list[i]]
    


def get_process_data(output_file):
    processes = []
    line_index= 0
    data_index=0
    cmd = subprocess.Popen('top -b -n 1', shell=True, stdout=subprocess.PIPE)
    for line in cmd.stdout:
        line_index+=1
        process_metrices = re.sub(' +', ' ', line.decode())
        if (PROCESS_METRICES_TITLES) in process_metrices:
            data_index=line_index
        if data_index!=0 and line_index>data_index:
            data = get_process_metric(process_metrices)
            processes.append(data)
    return processes


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_file', type=str, required=True)
    args = parser.parse_args()
    processes = get_process_data(args.output_file+'.txt')
    # print(processes)