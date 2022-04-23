import time
import argparse
from distutils.util import strtobool
from typing import Any

from Src.Apriori.main import apriori
from config import MIN_SUP, BEAT_FREQUENCY, FILE_PATH, FILE_PATH_TEST, FLAG_TEST


def read(flag_test) -> list[list[Any, set[int]]]:
    if flag_test:
        dat_file = open(FILE_PATH_TEST, "r")
    else:
        dat_file = open(FILE_PATH, "r")
    dat_text = dat_file.readlines()
    data_list = [set([n for n in l.split() if len(n) > 0]) for l in dat_text]
    raw_data = [[i + 1, d] for i, d in enumerate(data_list)]
    return raw_data


if __name__ == "__main__":
    augument_list = argparse.ArgumentParser()
    augument_list.add_argument("--min_sup", type=float, default=MIN_SUP)
    augument_list.add_argument(
        "--beat_frequency", type=int, default=BEAT_FREQUENCY
    )
    augument_list.add_argument("--flag_test", type=str, default=FLAG_TEST)
    MIN_SUP = augument_list.parse_args().min_sup
    BEAT_FREQUENCY = augument_list.parse_args().beat_frequency
    FLAG_TEST = bool(strtobool(augument_list.parse_args().flag_test))
    print("MIN_SUP:", MIN_SUP)
    print("BEAT_FREQUENCY:", BEAT_FREQUENCY)
    print("FLAG_TEST:", FLAG_TEST)

    raw_data = read(FLAG_TEST)
    # print(raw_data)
    start_time_global = time.time()
    apriori(raw_data, MIN_SUP, BEAT_FREQUENCY)
    end_time_global = time.time()
    print("Total time:", end_time_global - start_time_global)
