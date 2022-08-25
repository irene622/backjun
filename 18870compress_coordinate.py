num_num = int(input())
num_list = list(map(int, input().split()))

def make_num_dict(num_list) :
    distinct_dict = {}
    for i in set(num_list) :
        distinct_dict[i] = 0
    return distinct_dict


def comp_coordinates(num_num, num_list) :
    dist_dict = make_num_dict(num_list)
    num = len(set(num_list))
    dist_num_list = list(set(num_list))

    for i in range(num) :
        for side_idx in range(i+1, num) :
            if dist_num_list[i] < dist_num_list[side_idx] :
                dist_dict[dist_num_list[side_idx]] += 1
            elif dist_num_list[i] == dist_num_list[side_idx] :
                continue
            else :
                dist_dict[dist_num_list[i]] += 1
    return dist_dict


def print_result(num_num, num_list) :
    result = ''
    result_dict = comp_coordinates(num_num, num_list)
    for num in num_list :
        result += str(result_dict[num]) + ' '
    return result

print(print_result(num_num, num_list))