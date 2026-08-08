import math
def max_subarray_product_size_k(nums, k):
  curr_prod = math.prod(nums[0:k])
  max_prod = curr_prod

  for i in range(len(nums)-k):
    curr_prod = curr_prod // nums[i]
    curr_prod *= nums[i+k]

    if curr_prod > max_prod:
      max_prod = curr_prod

  return max_prod
