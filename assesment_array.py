def positive_numbers(nums):
    for num in nums:
        if num > 0:
            yield num

numbers = list(map(int, input().split()))
result = list(positive_numbers(numbers))
print(*result)