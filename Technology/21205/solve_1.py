def check_registration_rules(**kwargs):
    result = []
    for k, v in kwargs.items():
        if k == 'codecup' or k == 'quera':
            continue
        elif len(k) < 4:
            continue
        elif len(v) < 6 or str(v).isdecimal():
            continue
        else:
            result.append(k)
    return result
# Mohammad YousefiPour - Github.com/myp79
