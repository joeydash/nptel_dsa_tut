def rainaverage(arr):
    new_dict = {}
    new_array = []
    for item in arr:
        if item[0] in new_dict:
            new_dict[item[0]] = new_dict[item[0]] + [item[1]]
        else:
            new_dict[item[0]] = [item[1]]
    for item in sorted(new_dict.keys()):
        sum = 0
        count = 0
        for n_item in new_dict[item]:
            sum = sum + n_item
            count += 1
        new_array = new_array + [(item, sum / count)]
    return new_array


def flatten(m_list):
    new_list = []
    for item in m_list:
        if isinstance(item, list):
            new_list = new_list + flatten(item)
        else:
            new_list = new_list + [item]
    return new_list
