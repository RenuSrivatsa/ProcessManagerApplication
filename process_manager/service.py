import subprocess
import re
from constants import PROCESS_METRICES_TITLES
from utils import get_process_metric

class Service:
    def __init__(self):
        pass
    def get_process_data(self):
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