FILE_PATH=""
TID=0
RAW_DATA=[]

MIN_SUP=0.5

## INPUT DATA

def genTID():
    TID+=1
    return TID

def read():
    dat_file=open(FILE_PATH,"r")
    dat_text=dat_file.read()
    for i in range(len(dat_text)):
        RAW_DATA.append([genTID(),dat_text[i].split(" ")])

## COMPUTE

def is_in():
    # 例子：判断一个行[a,b,c,d,e]是否存在[a,m]，并返回false
    pass

def count_sup_for_C_list(raw_data, c_list):
    for i in range(len(raw_data)):
        for j in range(len(c_list)):
            if is_in(raw_data[i],c_list[j].data) :
                c_list[j].count+=1
    for i in range(len(c_list)):
        c_list[i].sup=c_list[i].count/len(raw_data)

def c_list_prune(c_list, MIN_SUP):
    new_c_list=[]
    for i in range(len(c_list)):
        if c_list[i].sup >= MIN_SUP:
            new_c_list.append(c_list[i])
    return new_c_list

#### COUNT


#### GenCi

#### PruneLi