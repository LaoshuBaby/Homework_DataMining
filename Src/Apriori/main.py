FILE_PATH=""
TID=0
RAW_DATA=[]

MIN_SUP=0.5

## INPUT DATA

def genTID():
    TID+=1
    return TID:int

def read():
    dat_file=open(FILE_PATH,r)
    dat_text=dat_file.read()
    for i in range(len(dat_text)):
        RAW_DATA.append([genTID(),dat_text[i].split(" ")])

## COMPUTE

#### COUNT


#### GenCi

#### PruneLi