#test branch

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


def main():
    for x in get_processes():
        print(list(x.values()))


if __name__ == "__main__":
    while True:
        main()

    # print(pd.DataFrame(get_processes()))
    # This prints in the default pandas format
