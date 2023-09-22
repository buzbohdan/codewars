"""CURRENTLY DOESNT WORK"""
def sum_of_intervals(intervals: list[list[int]]) -> int:
    merged = []
    for a, b in intervals:
        new_merged = []
        for merged_interval in merged:
            # No overlap
            if a > merged_interval[1] or merged_interval[0] > b:
                continue
            merged_interval[0] = min(a, merged_interval[0])
            merged_interval[1] = max(b, merged_interval[1])
            break
        else:
            merged.append([a, b])

    return sum([b - a for a, b in merged])

# s = sum_of_intervals([[1, 5]])
# assert s == 4

s = sum_of_intervals([[1, 5], [2, 3], [10, 11], [-10, -5], [-9, -6], [-1000, 1000]])
assert s == 10
