def average(array):
    unique_heights = set(array)
    total_sum = sum(unique_heights)
    count = len(unique_heights)
    return total_sum / count
