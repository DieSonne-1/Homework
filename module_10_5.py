import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline().strip()
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':
    start1 = datetime.now()
    for f in filenames:
        read_info(f)
    end1 = datetime.now()
    print(f'{end1 - start1} (Линейный)')

    with multiprocessing.Pool() as pool:
        start2 = datetime.now()
        pool.map(read_info, filenames)
        end2 = datetime.now()
        print(f'{end2 - start2} (Многопроцессорный)')

filenames = [f'./file {number}.txt' for number in range(1, 5)]
