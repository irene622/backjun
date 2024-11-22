import sys

line = sys.stdin.readline().strip()

result = ''
open = False
reversed_word = ''
for char in line:
    if open is False:
        if char == ' ':
            result += reversed_word[::-1]
            result += ' '
            reversed_word = ''
        elif char == '<':
            open = True
            if reversed_word != '':
                result += reversed_word[::-1]
                reversed_word = ''
            result += '<'
        else:
            reversed_word += char
    elif open is True:
        if char == '>':
            result += '>'
            open = False
        else:
            result += char

if reversed_word != '':
    result += reversed_word[::-1]

print(result)
