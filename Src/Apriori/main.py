def build_first_c_list(raw_data):
    c_list=set([])
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i][1])):
            c_list.add(raw_data[i][1][j])
    c_list=list(c_list)
    return c_list




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
    for i in range(len(l_list)):
        flag_not_exist=False
        for j in range(len(c_list)):
            if set(c_list[j].data).issubset(set(l_list[i].data)) == False:
                flag_not_exist = True
                break
        if flag_not_exist == True:
            l_list.pop(i)
    true_l_list=l_list
    return true_l_list

def apriori(RAW_DATA, MIN_SUP):
    print(build_first_c_list(RAW_DATA))


if __name__ == "__main__":
    exit(-1)

