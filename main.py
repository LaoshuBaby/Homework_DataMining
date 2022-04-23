import time
from typing import List, Set, Tuple, Any

from Src.Apriori.main import apriori

FILE_PATH = "D:\\retail.dat"
TEST_NAME = "apriori_paper_attached"
FILE_PATH_TEST = "Data/" + TEST_NAME + ".dat"
FLAG_TEST = True
RAW_DATA = []

MIN_SUP = 0.5 # Default

## INPUT DATA


def read() -> list[list[Any, set[int]]]:
    if FLAG_TEST:
        dat_file = open(FILE_PATH_TEST, "r")
    else:
        dat_file = open(FILE_PATH, "r")
    dat_text = dat_file.readlines()
    data_list = [set([n for n in l.split() if len(n) > 0]) for l in dat_text]
    RAW_DATA = [[i + 1, d] for i, d in enumerate(data_list)]
    return RAW_DATA


if __name__ == "__main__":
    # 加上参数读取，允许自定义MIN_SUP

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--min_sup', type=float, default=MIN_SUP)
    args = parser.parse_args()
    MIN_SUP = args.min_sup
    print("MIN_SUP:", MIN_SUP)

    raw_data = read()
    # print(raw_data)
    start_time_global = time.time()
    apriori(raw_data, MIN_SUP)
    end_time_global = time.time()
    print("Total time:", end_time_global - start_time_global)
