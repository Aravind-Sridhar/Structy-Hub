def subarray_target_sum_size_k(nums, target, k):
  result = 0
  curr_sum = sum(nums[0:k])
  if curr_sum == target:
    result+=1
  for i in range(len(nums)-k):
    curr_sum -= nums[i]
    curr_sum += nums[i+k]
    
    if curr_sum == target:
      result+=1
  return result