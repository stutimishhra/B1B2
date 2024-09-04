def analyze_numbers(numbers):
    cumulative_sum = 0
    min_value = float('inf')
    max_value = float('-inf')
    for num in numbers:
        cumulative_sum += num
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    average = cumulative_sum / len(numbers)
    return cumulative_sum, average, min_value, max_value
numbers = [11, 21, 31, 41, 51]
result = analyze_numbers(numbers)
print("Cumulative Sum:", result[0])
print("Average:", result[1])
print("Minimum Value:", result[2])
print("Maximum Value:", result[3])