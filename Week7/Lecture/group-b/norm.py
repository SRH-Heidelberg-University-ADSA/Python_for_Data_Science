def normalize(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# result = normalize([20, 24, 25])
# print(result)
