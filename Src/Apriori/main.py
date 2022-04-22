from Src.Apriori.user_class import Itemset


def print_list(lst):
    for i in range(len(lst)):
        print(lst[i])
    print("======", "len=" + str(len(lst)))


def c_list_enum_collect(raw_data):
    c_enum = set()
    for i in range(len(raw_data)):
        single_line=list(raw_data[i][1])
        for j in range(len(single_line)):
            c_enum.add(single_line[j])
    c_enum = list(c_enum)
    c_list = []
    for i in range(len(c_enum)):
        c_list.append(Itemset(data=set(c_enum[i]), count=0, sup=0))
    return c_list


def c_list_sup_count(raw_data, c_list):
    for i in range(len(raw_data)):
        for j in range(len(c_list)):
            if set(c_list[j].data).issubset(raw_data[i][1]):
                c_list[j].count += 1
    for i in range(len(c_list)):
        c_list[i].sup = c_list[i].count / len(raw_data)
    # 这个地方最好能对c_list进行排序，按照data里面各个元素的字典序
    # c_list=
    return c_list


def c_list_prune(c_list, MIN_SUP):
    new_c_list = []
    for i in range(len(c_list)):
        if c_list[i].sup >= MIN_SUP:
            new_c_list.append(c_list[i])
    return new_c_list


def l_list_pre_combine(c_list):
    l_list = []
    for i in range(len(c_list)):
        for j in range(i, len(c_list)):
            if i != j:
                itemset_ready=Itemset(
                        data=set(c_list[i].data).union(set(c_list[j].data)),
                        sup=0,
                        count=0,
                    )
                def itemset_not_in_list(itemset_x, l_list):
                    flag_not_in_list=True
                    for j in range(len(l_list)):
                        if l_list[j].data==itemset_x.data:
                            return False
                    if flag_not_in_list==True:
                        return True
                if itemset_not_in_list(itemset_ready,l_list):
                    l_list.append(itemset_ready)
    return l_list


def l_list_prune(l_list, c_list):
    # 输入对应的clist，对llist的每一个项集都拆开看其子集是否全都在clist里，有不合法的就毙掉这个llist中的项集
    print(len(l_list),len(c_list))
    true_l_list=[]
    for i in range(len(l_list)):
        flag_not_exist = False
        for j in range(len(c_list)):
            print(
                "l_list["+str(i)+"]="+str(set(l_list[i].data)),
                "c_list["+str(j)+"]="+str(set(c_list[j].data)),
                set(c_list[j].data).issubset(set(l_list[i].data))
            )
            def gen_full_subset_list(set_x):
                set_x_list=list(set_x)
                # 使用二进制法生成所有子集
                subset_list=[]
                for i in range(len(set_x)):
                    # 把i转成二进制,补齐长度到len(set_x)
                    i_bin=str(bin(i)).replace("0b","")
                    while len(i_bin)<len(set_x):
                        i_bin="0"+i_bin
                    #print(i_bin)
                    # 提取1对应的set_x_list中的元素
                    i_bin_list=[]
                    for j in range(len(set_x)):
                        if i_bin[j]=="1":
                            i_bin_list.append(set_x_list[j])
                    #print(i_bin_list)
                    # 把提取出来的元素打包作为一个集合，添加到subset_list中
                    if i_bin_list != []:
                        subset_list.append(set(i_bin_list))
                return subset_list
            print(gen_full_subset_list(set(l_list[i].data)))
            if set(c_list[j].data).issubset(set(l_list[i].data)) == False:
                flag_not_exist = True
                break
        if flag_not_exist != True:
            true_l_list.append(l_list[i])
    return true_l_list


def apriori(RAW_DATA, MIN_SUP):
    # 预热遍历生成空的所有待计算支持度的元素列表
    c0_status = c_list_enum_collect(RAW_DATA)
    print_list(c0_status)

    # 循环内执行
    def gen_next_level(current_level:int, c_list):
        c_out=c_list_sup_count(RAW_DATA, c_list)
        print_list(c_out)
        l_out = c_list_prune(c_out, MIN_SUP)
        print_list(l_out)
        if current_level != 0:
            next_level_withoutprune = l_list_pre_combine(l_out)
            print_list(next_level_withoutprune)
            next_level = l_list_prune(next_level_withoutprune, l_out)
            print_list(next_level)
        else:
            next_level= l_list_pre_combine(l_out)
            print_list(next_level)

        return c_out, l_out, next_level

    print("THE FIRST RUN")
    c1_status=gen_next_level(0, c0_status)
    print("THE SECOND RUN")
    c2_status=gen_next_level(1, c1_status[2])


if __name__ == "__main__":
    exit(-1)
