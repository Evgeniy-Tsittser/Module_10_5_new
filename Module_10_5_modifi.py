import multiprocessing
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            all_data.append(line)
            line = f.readline()
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = time()

for file in filenames:
    read_info(file)

end_time = time()
print(end_time-start)

"""
def run(filenames):
    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, filenames)

if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start = time()
    run(filenames)

    end = time()
    print(end - start)
"""