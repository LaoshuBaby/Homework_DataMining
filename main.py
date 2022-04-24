import time
import argparse
from distutils.util import strtobool
from typing import Any

from Src.Apriori.main import apriori
from config import MIN_SUP, BEAT_FREQUENCY, FILE_PATH, FILE_PATH_TEST, FLAG_TEST, NO_CACHE, ONLY_FINAL


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
    argument_list = argparse.ArgumentParser()
    argument_list.add_argument("--min_sup", type=float, default=MIN_SUP)
    argument_list.add_argument(
        "--beat_frequency", type=int, default=BEAT_FREQUENCY
    )
    argument_list.add_argument("--flag_test", type=str, default=FLAG_TEST)
    argument_list.add_argument("--no_cache", type=str, default=NO_CACHE)
    argument_list.add_argument("--only_final", type=str, default=ONLY_FINAL)
    MIN_SUP = argument_list.parse_args().min_sup
    BEAT_FREQUENCY = argument_list.parse_args().beat_frequency
    FLAG_TEST = bool(strtobool(argument_list.parse_args().flag_test))
    NO_CACHE = bool(strtobool(argument_list.parse_args().no_cache))
    ONLY_FINAL = bool(strtobool(argument_list.parse_args().only_final))
    print("MIN_SUP:", MIN_SUP)
    print("BEAT_FREQUENCY:", BEAT_FREQUENCY)
    print("FLAG_TEST:", FLAG_TEST)
    print("NO_CACHE:", NO_CACHE)
    print("ONLY_FINAL:", ONLY_FINAL)

    raw_data = read(FLAG_TEST)
    # print(raw_data)
    start_time_global = time.time()
    apriori(raw_data, MIN_SUP, BEAT_FREQUENCY,ONLY_FINAL,NO_CACHE)
    end_time_global = time.time()
    print("Total time:", end_time_global - start_time_global)
