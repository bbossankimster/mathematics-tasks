from itertools import accumulate

def highest_sum_range(data):
    max_val, min_val = max(data), min(data)
    if min_val >= 0 and max_val >= 0:
        return (0, len(data)-1)
    elif min_val < 0 and max_val < 0:
        return (data.index(max_val), data.index(max_val))
    else:
        highest_sum = sum(data)
        num_count = len(data)
        res = None
        for i in range(num_count):
            acc_sums = list(accumulate(data[i:]))
            if max(acc_sums) > highest_sum:
                highest_sum = max(acc_sums)
                res = (i, i + acc_sums.index(max(acc_sums)))
        if res:
            return res
        else:
            return (0, len(data)-1)


# 100, 1, 1, -100, 100