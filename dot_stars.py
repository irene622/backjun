star = '***\n* *\n***\n'
blank = '   \n   \n   \n'

def stars(n) :
    if n == 3 :
        return star.split('\n')
    else :
        blank = '   \n' * n
        print(stars(n/3) + stars(n/3) + stars(n/3)) + print(stars(n/3) + blank + stars(n/3))
        print(stars(n/3) + stars(n/3) + stars(n/3))
    return

def main() :
    num = int(input())
    ans = stars(num)
    for i in ans :
        print(i)

main()