import time
from typing import List, Set, Tuple, Any

from Src.Apriori.main import apriori

FILE_PATH = "D:\\retail.dat"
TEST_NAME="apriori_paper_attached"
FILE_PATH_TEST = "Data/"+TEST_NAME+".dat"
FLAG_TEST = False
RAW_DATA = []

MIN_SUP = 0.001

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
    raw_data = read()
    # print(raw_data)
    start_time = time.time()
    apriori(raw_data, MIN_SUP)
    end_time = time.time()
    print("Time taken:", end_time - start_time)
