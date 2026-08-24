def longest_subarray_sum(nums, target_sum):
  curr_sum = 0
  start = 0
  largest = -1

  for end in range(len(nums)):
    curr_sum += nums[end]

    while curr_sum > target_sum:
      curr_sum -=nums[start]
      start+=1

    if curr_sum == target_sum and ((end-start)+1) > largest:
      largest = (end-start)+1


  return largest