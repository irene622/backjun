num_num = int(input())
num_list = map(input().split(), int)

[3,2,1,3,2,1]
[2,1,0,2,1,0]

[2, 4, -10, 4, -9]
[2, 3, 0, 3, 1]

def comp_coordinates(num_num, num_list) :
    result = [0] * num_num
    for i in range(num_num) :
        for side_idx in range(i, num_num) :
            if num_list[i] < num_list[side_idx] :
                result[side_idx] += 1
            else :
                result[i] = len(set(num_list)) - 1
    return result

print(comp_coordinates(num_num, num_list))