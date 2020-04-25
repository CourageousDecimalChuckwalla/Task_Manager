# Initial Commit
# test

import sys
# sys module contains os module
import pandas as pd
import psutil
import datetime as dt
import time


def get_processes():
    processes = []

    for process in psutil.process_iter():
        with process.oneshot():
            pid = process.pid
            name = process.name()

            if pid == 0:  # Filter out System Idle Process
                continue

        processes.append({
            'pid': pid,
            'name': name
        })

    return processes


if __name__ == "__main__":
    for x in get_processes():
        print(list(x.values()))

