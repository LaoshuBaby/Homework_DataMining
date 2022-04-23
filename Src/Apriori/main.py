import time

from Src.Apriori.user_class import Itemset

BEAT_FREQUENCY=""

def print_list(lst, output="optional"):
    # print("[BEAT]Print List")
    for i in range(len(lst)):
        if len(lst) <= BEAT_FREQUENCY or output == "mandatory":
            print(lst[i])
    if BEAT_FREQUENCY != 0 or output == "mandatory":
        print("======", "len=" + str(len(lst)))


def c_list_enum_collect(raw_data):
    c_enum = set()
    for i in range(len(raw_data)):
        single_line = list(raw_data[i][1])
        for j in range(len(single_line)):
            c_enum.add(single_line[j])
        if BEAT_FREQUENCY != 0:
            if i % (100 * BEAT_FREQUENCY) == 0:
                print("[BEAT]Calc Enum" + str(i))
    c_enum = list(c_enum)
    print(c_enum)  # debug
    c_list = []
    for i in range(len(c_enum)):
        c_list.append(Itemset(data=set([c_enum[i]]), count=0, sup=0))
        if BEAT_FREQUENCY != 0:
            if i % (100 * BEAT_FREQUENCY) == 0:
                print("[BEAT]Calc Enum" + str(i))
    return c_list


def c_list_sup_count(raw_data, c_list):
    # 在逐行的原始数据中统计若干个项集各种出现的总次数
    for i in range(len(raw_data)):
        for j in range(len(c_list)):
            if set(c_list[j].data).issubset(raw_data[i][1]):
                c_list[j].count += 1
        if BEAT_FREQUENCY != 0:
            if i % (10 * BEAT_FREQUENCY) == 0:
                print("[BEAT]Calc Support" + str(i))  # 性能优化重点关照
    # 统计每个候选项集支持度
    for i in range(len(c_list)):
        c_list[i].sup = c_list[i].count / len(raw_data)
        if BEAT_FREQUENCY != 0:
            if i % (10 * BEAT_FREQUENCY) == 0:
                print("[BEAT]Calc Support" + str(i))

    # 如果能顺便按照data里面各个元素的字典序对c_list进行排序是最好
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
                itemset_ready = Itemset(
                    data=set(c_list[i].data).union(set(c_list[j].data)),
                    sup=0,
                    count=0,
                )

                def itemset_not_in_list(itemset_x, l_list):
                    flag_not_in_list = True
                    for j in range(len(l_list)):
                        if l_list[j].data == itemset_x.data:
                            return False
                    if flag_not_in_list == True:
                        return True

                if itemset_not_in_list(itemset_ready, l_list):
                    l_list.append(itemset_ready)
    return l_list


def l_list_prune(l_list, c_list):
    # 输入对应的clist，对llist的每一个项集都拆开看其子集是否全都在clist里，有不合法的就毙掉这个llist中的项集
    print(len(l_list), len(c_list))
    true_l_list = []
    for i in range(len(l_list)):
        flag_not_exist = False
        for j in range(len(c_list)):
            # 判断应不应该修建
            def gen_full_subset_list(set_x):
                set_x_list = list(set_x)
                # 使用二进制法生成所有子集
                subset_list = []
                for i in range(pow(2, len(set_x))):
                    # 把i转成二进制,补齐长度到len(set_x)
                    i_bin = str(bin(i)).replace("0b", "")
                    while len(i_bin) < len(set_x):
                        i_bin = "0" + i_bin
                    if i_bin.count("1") != len(set_x) - 1:
                        continue
                    # print(i_bin)
                    # 提取1对应的set_x_list中的元素
                    i_bin_list = []
                    for j in range(len(set_x)):
                        if i_bin[j] == "1":
                            i_bin_list.append(set_x_list[j])
                    # print(i_bin_list)
                    # 把提取出来的元素打包作为一个集合，添加到subset_list中
                    if i_bin_list != []:
                        subset_list.append(set(i_bin_list))
                return subset_list

            full_subset_list = gen_full_subset_list(set(l_list[i].data))

            def set_not_in_list(set_x, list_x):
                flag_found = False
                for i in range(len(list_x)):
                    if set(list_x[i].data) == set_x:
                        flag_found = True
                    else:
                        continue
                if flag_found == False:
                    return True
                else:
                    return False

            flag_have_invaild_subset = False
            for k in range(len(full_subset_list)):
                if set_not_in_list(full_subset_list[k], c_list) == True:
                    flag_have_invaild_subset = True
        if flag_have_invaild_subset == False:
            true_l_list.append(l_list[i])

    return true_l_list


def apriori(RAW_DATA, MIN_SUP, BEAT_FREQUENCY_THRESHOLD):
    global BEAT_FREQUENCY
    BEAT_FREQUENCY=BEAT_FREQUENCY_THRESHOLD
    start_time_first = time.time()
    # 预热遍历生成空的所有待计算支持度的元素列表
    c0_status = c_list_enum_collect(RAW_DATA)
    # print_list(c0_status)
    end_time_first = time.time()
    print("[0]Pre calc C1 time:", end_time_first - start_time_first)

    # 循环内执行
    def gen_next_level(current_level: int, c_list):
        start_time_level = time.time()
        if len(c_list) == 0:
            return [], [], 0

        start_time_c_list = time.time()
        c_out = c_list_sup_count(RAW_DATA, c_list)
        print_list(c_out)
        end_time_c_list = time.time()
        print(
            "[1]Gen C" + str(current_level + 1) + " time:",
            end_time_c_list - start_time_c_list,
        )

        start_time_l_list = time.time()
        l_out = c_list_prune(c_out, MIN_SUP)
        print_list(l_out)
        end_time_l_list = time.time()
        print(
            "[2]Gen L" + str(current_level + 1) + " time:",
            end_time_l_list - start_time_l_list,
        )
        if current_level != 0:
            # 预组合项集
            start_time_pre_combine = time.time()
            next_level_withoutprune = l_list_pre_combine(l_out)
            print_list(next_level_withoutprune)
            end_time_pre_combine = time.time()
            print(
                "[3]Pre combine time:",
                end_time_pre_combine - start_time_pre_combine,
            )
            # 修剪存在非频繁子集的项集
            start_time_prune = time.time()
            next_level = l_list_prune(next_level_withoutprune, l_out)
            print_list(next_level)
            end_time_prune = time.time()
            print("[4]Prune time:", end_time_prune - start_time_prune)
        else:
            # 预组合项集
            start_time_pre_combine = time.time()
            next_level = l_list_pre_combine(l_out)
            print_list(next_level)
            end_time_pre_combine = time.time()
            print(
                "[3]Pre combine time:",
                end_time_pre_combine - start_time_pre_combine,
            )

        print(
            "The " + str(current_level + 1) + " round run total time:",
            time.time() - start_time_level,
        )
        return c_out, l_out, next_level

    print("THE FIRST RUN")
    c1_status = gen_next_level(0, c0_status)
    print("THE SECOND RUN")
    c2_status = gen_next_level(1, c1_status[2])
    print("THE THIRD RUN")
    c3_status = gen_next_level(2, c2_status[2])
    print("THE FOURTH RUN")
    c4_status = gen_next_level(3, c3_status[2])
    print("THE FIFTH RUN")
    c5_status = gen_next_level(3, c3_status[2])

    print("$$$$$$[FINAL RESULT]$$$$$$")

    def final(status, i):
        if len(status[0]) != 0:
            print("C" + str(i) + ":")
            print_list(status[0], output="mandatory")
        if len(status[1]) != 0:
            print("L" + str(i) + ":")
            print_list(status[1], output="mandatory")

    for i in range(1, 5):
        final(eval("c" + str(i) + "_status"), i)
    print("$$$$$$[FINAL RESULT]$$$$$$")
    sum_itemset=0
    for i in range(1,5):
        sum_itemset+=len(eval("c"+str(i)+"_status")[1])
    print("Min support= "+str(MIN_SUP)+"\nThe sum of itemset: "+str(sum_itemset))
    print("$$$$$$[FINAL RESULT]$$$$$$")


if __name__ == "__main__":
    exit(-1)
