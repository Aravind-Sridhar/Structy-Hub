## max subarray sum size k

Write a function that takes in a list of numbers and a size k as arguments. The function should return the maximum sum
of subarrays that contain exactly k elements.

You can assume that k is less than or equal to the length of the input list.

#### test_00:

```python
max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3) # -> 15
# [8,4,3] is the subarray of size 3 with the maximal sum
```

#### test_01:

```python
max_subarray_sum_size_k([2, 1, 5, -4, 6] , 3) # -> 8
```

#### test_02:

```python
max_subarray_sum_size_k([1, 4, 1, 10, 25, 3, 1, 0, 20], 4) # -> 40
```

#### test_03:

```python
max_subarray_sum_size_k([20, 50, 10, 60, 80, 70], 1) # -> 80
```

#### test_04:

```python
max_subarray_sum_size_k([-4, -18, -2, -5, -9], 2) # -> -7
```

#### test_05:

```python
nums = [1] * 10000 # [1,1,1,1,...]
max_subarray_sum_size_k(nums, 1000) # -> 1000
```

#### test_06:

```python
nums = [1] * 80000 # [1,1,1,1,...]
max_subarray_sum_size_k(nums, 5000) # -> 5000
```
