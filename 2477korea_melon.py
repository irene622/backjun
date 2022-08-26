num_korea_melon = int(input())
direction = []
distance = []
for _ in range(6) :
    dire, dis = list(map(int, input().split()))
    direction.append(dire)
    distance.append(dis)

def cal_large_area(direction, distance) :
    horizontal = 0
    vertical = 0
    for i in range(6) :
        if direction[i] == 1 :
            horizontal += distance[i]
        if direction[i] == 3 :
            vertical += distance[i]
    large_area = horizontal * vertical
    return large_area


def find_multiple_index(one_dir, direction) :
    if direction.count(one_dir) != 1 :
        return list(filter(lambda x: direction[x] == one_dir, range(6)))
    return None

def cal_small_area(direction, distance) :
    small = []
    for i in range(1,5) :
        if find_multiple_index(i, direction) is not None :
            small.append(find_multiple_index(i, direction))

    if small[0][0] > small[1][0] :
        small_area = distance[small[0][0]] * distance[small[1][1]]
    else :
        small_area = distance[small[0][1]] * distance[small[1][0]]
    return small_area


def main() :
    area = cal_large_area(direction, distance) - cal_small_area(direction, distance)
    result = num_korea_melon * area
    return result

print(main())