from Src.Apriori.user_class import Itemset

def print_list(lst):
    for i in range(len(lst)):
        print(lst[i])
    print("======","len="+str(len(lst)))


def c_list_enum_collect(raw_data):
    c_list=set([])
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i][1])):
            c_list.add(raw_data[i][1][j])
    c_list_pre=list(c_list)
    c_list=[]
    for i in range(len(c_list_pre)):
        c_list.append(Itemset(data=[c_list_pre[i]],count=0,sup=0))
    return c_list




def c_list_sup_count(raw_data, c_list):
    for i in range(len(raw_data)):
        for j in range(len(c_list)):
            if set(c_list[j].data).issubset(set(raw_data[i][1])):
            # if is_in(raw_data[i][1],c_list[j].data) :
                c_list[j].count+=1
    for i in range(len(c_list)):
        c_list[i].sup=c_list[i].count/len(raw_data)
    # 这个地方最好能对c_list进行排序，按照data里面各个元素的字典序
    # c_list=
    return c_list

def c_list_prune(c_list, MIN_SUP):
    new_c_list=[]
    for i in range(len(c_list)):
        if c_list[i].sup >= MIN_SUP:
            new_c_list.append(c_list[i])
    return new_c_list


def l_list_pre_combine(c_list):
    # 构建出所有可能的子集的组合,目前这步有重复

    l_list=[]
    for i in range(len(c_list)):
        for j in range(i,len(c_list)):
            if i!=j:
                l_list.append(Itemset(
                    data=set(c_list[i].data).union(set(c_list[j].data)),
                    sup=0,
                    count=0
                ))
    return l_list

#### PruneLi

def l_list_prune(l_list,c_list):
    # 输入对应的clist，对llist的每一个项集都拆开看其子集是否全都在clist里，有不合法的就毙掉这个llist中的项集
    for i in range(len(l_list)):
        flag_not_exist=False
        for j in range(len(c_list)):
            print("i="+str(i)+" j="+str(j))
            if set(c_list[j].data).issubset(set(l_list[i].data)) == False:
                flag_not_exist = True
                break
        if flag_not_exist == True:
            l_list.pop(i)
    true_l_list=l_list
    return true_l_list

def apriori(RAW_DATA, MIN_SUP):
    # 预热遍历生成空的所有待计算支持度的元素列表
    c0=c_list_enum_collect(RAW_DATA)
    #print_list(c0)

    # 循环内执行
    c1=c_list_prune(c_list_sup_count(RAW_DATA, c0), MIN_SUP)
    print_list(c1)
    l1=l_list_pre_combine(c1)
    print_list(l1)
    l1=l_list_prune(l1,c1)
    print_list(l1)

if __name__ == "__main__":
    exit(-1)

