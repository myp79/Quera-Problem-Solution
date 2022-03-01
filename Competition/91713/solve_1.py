def is_mirror(phone):
    if phone == phone[::-1]:
        return True
    return False


def is_threeNum(phone):
    if '000' in phone or '111' in phone or '222' in phone or '333' in phone or '444' in phone or '555' in phone or '666' in phone or '777' in phone or '888' in phone or '999' in phone:
        return True
    return False


def is_repeat(phone):
    d = {}
    for index in phone:
        d[index] = d.get(index, 0) + 1

    for index in d.values():
        if index >= 4:
            return True
    return False


t = int(input())
phone_list = []
for i in range(t):
    phone_list.append(input())

for phone in phone_list:
    if is_threeNum(phone):
        print('Ronde!')
    elif is_repeat(phone):
        print('Ronde!')
    elif is_mirror(phone):
        print('Ronde!')
    else:
        print('Rond Nist')
# Mohammad YousefiPour - Github.com/myp79
