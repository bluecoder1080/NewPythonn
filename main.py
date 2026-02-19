def find_max(numbers):
    max = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max = numbers[i]

    return max


nums = [5, 8, 2, 15, 3]

result = find_max(nums)

print("Maximum number is:", result)

print("Length is " + len(nums))
