def dot_stars(n) :
    if n == 1:
        return ['*']
    else :
        stars = dot_stars(n/3)
        result = []

        for star in stars :
            result.append(star*3)
        for star in stars :
            temp_result = star + ' '*int(n/3) + star
            result.append(temp_result)
        for star in stars :
            result.append(star*3)

    return result


def main() :
    num = int(input())
    ans = dot_stars(num)
    for line in ans :
        print(line)

main()