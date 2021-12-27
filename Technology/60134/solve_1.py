def fruits(fruit_list):
    d = {}
    for index in fruit_list:
        if index['shape'] == 'sphere':
            if 300 <= index['mass'] <= 600:
                if 100 <= index['volume'] <= 500:
                    d[index['name']] = d.get(index['name'], 0)+1
    return d
