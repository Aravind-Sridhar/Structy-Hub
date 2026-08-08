## max subarray product size k

Write a function that takes in a list of numbers and a size k as arguments. The function should return the maximum product
of subarrays that contain exactly k elements.

You can assume that k is less than or equal to the length of the input list.

You can assume that numbers of the list are non-zero.

#### test_00:

```python
max_subarray_product_size_k([4, 2, 1, -9, 8, 2, 3], 3) # -> 48
# [8,2,3] is the subarray of size 3 with the maximal product
```

#### test_01:

```python
max_subarray_product_size_k([-9, 1, -8, 2, 3, 7], 3) # -> 72
```

#### test_02:

```python
max_subarray_product_size_k([7, 4, -5, -7, 8, -10, -1], 2) # -> 35
```

#### test_03:

```python
max_subarray_product_size_k([60, 20, 10, 90, 50], 1) # -> 90
```

#### test_04:

```python
max_subarray_product_size_k([1,2,3,4], 4) # -> 24
```

#### test_05:

```python
nums = [1] * 9000 # [1,1,1,...]
max_subarray_product_size_k(nums, 1000) # -> 1
```

#### test_06:

```python
nums = [1] * 40000 # [1,1,1,...]
max_subarray_product_size_k(nums, 5000) # -> 1
```
