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
    dat_text=dat_file.read()
    for i in range(len(dat_text)):
        RAW_DATA.append([genTID(),dat_text[i].split(" ")])
    return RAW_DATA

## COMPUTE

def is_in():
    # 例子：判断一个行[a,b,c,d,e]是否存在[a,m]，并返回false
    pass

def build_first_c_list(raw_data):
    c_list=set([])
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i][1])):
            c_list.add(raw_data[i][1][j])
    c_list=list(c_list)
    return c_list

#### COUNT


#### GenCi

def count_sup_for_C_list(raw_data, c_list):
    for i in range(len(raw_data)):
        for j in range(len(c_list)):
            if is_in(raw_data[i][1],c_list[j].data) :
                c_list[j].count+=1
    for i in range(len(c_list)):
        c_list[i].sup=c_list[i].count/len(raw_data)

def c_list_prune(c_list, MIN_SUP):
    new_c_list=[]
    for i in range(len(c_list)):
        if c_list[i].sup >= MIN_SUP:
            new_c_list.append(c_list[i])
    return new_c_list


def build_pre_l_list(c_list):
    # 构建出所有可能的子集组合
    return l_list

#### PruneLi

def l_list_prune(l_list,c_list):
    # 输入对应的clist，对llist的每一个项集都拆开看其子集是否全都在clist里，有不合法的就毙掉这个llist中的项集
    return true_l_list


if __name__ == "__main__":
    raw_data=read()
    print(raw_data)