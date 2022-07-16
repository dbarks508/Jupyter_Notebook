import multiprocessing
import os
import time
import random

def display_time(this_moment):
    print(f'its currently {this_moment}')

if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=display_time, args=(time.ctime(time.time()),))
        p.start()
        time.sleep(random.randint(0,1))
