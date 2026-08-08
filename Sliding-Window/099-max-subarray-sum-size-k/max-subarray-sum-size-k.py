def max_subarray_sum_size_k(nums, k):
  curr_sum = sum(nums[0:k])
  max_sum = curr_sum

  #Brute force timeout
  # for i in range(len(nums)-k+1):
  #   if max_sum < sum(nums[i:i+k]):
  #     max_sum = sum(nums[i:i+k])

  # return max_sum

  for i in range(len(nums)-k):
    curr_sum -= nums[i] 
    curr_sum += nums[i+k]
    if curr_sum > max_sum:
      max_sum = curr_sum

  return max_sum
  

  
