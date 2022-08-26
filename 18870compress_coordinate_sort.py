num_num = int(input())
num_list = list(map(int, input().split()))
dist_num_list = list(set(num_list))
# python list.sort = merge sort in blogs... :(
dist_num_list.sort()

compressed_coordinates = {}
for i in range(len(dist_num_list)) :
    compressed_coordinates[dist_num_list[i]] = i

for num in num_list :
    print(compressed_coordinates[num], end=' ')