import multiprocessing
import os
import time
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))


def task_sleep(sleep_duration, task_number):
    time.sleep(sleep_duration)
    print(f"Task {task_number} done (slept for {sleep_duration}s)! "
          f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    time_start = time.time()


    num_cpu = multiprocessing.cpu_count() - 1
    pool = multiprocessing.Pool(processes=num_cpu)


    pool.starmap(func=task_sleep, iterable=[(2, 1)] * 10)

    pool.close()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")
