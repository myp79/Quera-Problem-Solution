
def compress(code):
    final = ''
    final_test = code
    while(True):
        d = {}
        l = []
        result = []
        for digit in final_test:
            l.append(digit)
            d[digit] = d.get(digit, 0)+1

        sett = set(l)

        r = list(sett)
        for index in r:
            ind = d.get(index)
            if ind >= 2:
                result.append(str(ind))
                result.append(index)
            else:
                result.append(index)

        result.sort()
        final_test = ''.join(result)
        if final == final_test:
            break
        else:
            final = final_test

    return final


code = input()

print(compress(code))
# Mohammad YousefiPour - Github.com/myp79
