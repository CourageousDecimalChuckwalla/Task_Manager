import sys
# sys module contains os module
import pandas as pd
import psutil
from datetime import datetime
import time


# Outputs name, pid, cpu_usage, memory_usage, read/write bytes, status, create_time, thread, cores
# Implemented: name, pid, creation time

def get_processes():
    processes = []

    for process in psutil.process_iter():
        with process.oneshot():
            pid = process.pid
            name = process.name()

            if pid == 0:  # Filter out System Idle Process
                continue

            create_time = datetime.fromtimestamp(process.create_time())
        processes.append({
            'pid': pid,
            'name': name,
            'time': create_time.strftime("%c")
        })

    return processes


if __name__ == "__main__":
    for x in get_processes():
        print(list(x.values()))


# References
# https://www.thepythoncode.com/article/make-process-monitor-python
#   Raw Code: https://www.thepythoncode.com/code/make-process-monitor-python
#   Github: https://github.com/x4nth055/pythoncode-tutorials/tree/master/general/process-monitor