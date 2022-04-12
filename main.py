import time
from Src.Apriori.main import apriori

FILE_PATH="D:\\retail.dat"
TID=0
RAW_DATA=[]

MIN_SUP=0.5

## INPUT DATA

def genTID():
    global TID
    TID+=1
    return TID

def read():
    dat_file=open(FILE_PATH,"r")
    dat_text=dat_file.readlines()
    for i in range(len(dat_text)):
        RAW_DATA.append([genTID(),dat_text[i].split(" ")[:-1]])
    return RAW_DATA

if __name__ == "__main__":
    raw_data = read()
    print(raw_data)
    start_time = time.time()
    apriori(raw_data,MIN_SUP)
    end_time = time.time()
    print("Time taken:",end_time-start_time)