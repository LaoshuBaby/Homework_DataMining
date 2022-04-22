import time

from Src.Apriori.main import apriori

FILE_PATH = "D:\\retail.dat"
FILE_PATH_TEST = "Src/Apriori/test.dat"
FLAG_TEST = True
TID = 0
RAW_DATA = []

MIN_SUP = 0.5

## INPUT DATA


def genTID():
    global TID
    TID += 1
    return TID


def read():
    if FLAG_TEST:
        dat_file = open(FILE_PATH_TEST, "r")
    else:
        dat_file = open(FILE_PATH, "r")
    dat_text = dat_file.readlines()
    for i in range(len(dat_text)):
        dat_list = dat_text[i].split(" ")
        dat_list_clear = []
        for i in dat_list:
            if "\n" in i:
                i = i.replace("\n", "")
            if i != "":
                dat_list_clear.append(i)
        RAW_DATA.append([genTID(), set(dat_list_clear)])
    return RAW_DATA


if __name__ == "__main__":
    raw_data = read()
    print(raw_data)
    start_time = time.time()
    apriori(raw_data, MIN_SUP)
    end_time = time.time()
    print("Time taken:", end_time - start_time)
