def find_subarray_sum(nums, target_sum):
  start = 0
  win_sum = 0

  for end in range(len(nums)):
    win_sum += nums[end] # add to current window sum
  
    while win_sum > target_sum: #initalizing a while loop to iterate and modifying start i
      win_sum-=nums[start]
      start+=1

    if win_sum == target_sum:
      return (start,end)




  