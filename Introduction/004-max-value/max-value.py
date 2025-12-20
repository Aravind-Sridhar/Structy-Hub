def max_value(nums):
  max_val = -float('inf')
  for num in nums:
    if num > max_val:
      max_val = num
  return max_val