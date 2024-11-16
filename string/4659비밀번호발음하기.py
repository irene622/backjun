import sys

sys.stdin = open('string/4659.txt', 'r')

aeiou = 'aeiou'
bcdfg = "bcdfghjklmnpqrstvwxyz"
while True:
    line = sys.stdin.readline().strip()
    if line == 'end':
        break

    aeiou_count = 0
    in_a_row = 1
    prev_char = ''
    justify = True

    for character in line:
        if character in aeiou:
            aeiou_count += 1

        if prev_char != '':
            if prev_char in aeiou and character in aeiou:
                in_a_row += 1
            elif prev_char in aeiou and character not in aeiou:
                in_a_row = 1
            elif prev_char not in aeiou and character in aeiou:
                in_a_row = 1
            elif prev_char not in aeiou and character not in aeiou:
                in_a_row += 1
        if in_a_row >= 3:
            justify = False
            break
        
        if prev_char == character:
            if prev_char == 'e' or prev_char == 'o':
                continue
            else:
                justify = False
                break
        prev_char = character

    if aeiou_count == 0:
        justify = False
        
    if justify == False:
        print(f'<{line}> is not acceptable.')
    else:
        print(f'<{line}> is acceptable.')






