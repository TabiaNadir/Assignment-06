class Logger:
    def __init__(self):
        print("Logger initialized: Object created.")

    def __del__(self):
        print("Logger terminated: Object destroyed.")

log = Logger()
del log

import time
time.sleep(1)
