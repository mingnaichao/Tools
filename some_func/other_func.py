def divide_list(values, group=500):
    """
    将列表按指定大小进分组
    :param values:
    :param group:
    :return:
    """
    result_list = []
    if len(values) > group:
        sizes = range(0, len(values), group)
        pre = None
        cur = 0
        for cur in sizes:
            if pre is None and cur < len(values):
                pre = cur
                continue
            else:
                result_list.append(values[pre:cur])
                pre = cur
        if cur < len(values):
            result_list.append(values[cur:])
    else:
        result_list.append(values)
    return result_list


print(divide_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
