# unit test


def mean(numbers):
    return sum(numbers) / len(numbers)


def normalize(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    return [(x - min - val / max_val - min_val) for x in numbers]
