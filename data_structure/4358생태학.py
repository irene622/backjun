import sys

sys.stdin = open("data_structure/ex.txt")
info = {}
total = 0

while True:
    name = sys.stdin.readline().strip()
    if name == "":
        break

    total += 1
    if info.get(name) is None:
        info[name] = 1
    else:
        info[name] += 1


sorted_info = sorted(info.items(), key=lambda item: item[0])

for k, v in sorted_info:
    print(f"{k} {v/total*100:.4f}")
