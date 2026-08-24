## longest subarray sum

Write a function that takes in an list and a target sum. The function should return the length of the longest subarray
that sums to the target.

You can assume that the elements of the list are nonnegative.

If there is no subarray that sums to the target, then return -1.

#### test_00:

```python
longest_subarray_sum([1, 2, 1, 5, 2, 3, 10, 1, 9, 4, 3, 3, 7], 10) # -> 4
# the longest subarray with a sum of 10 is [2, 1, 5, 2] and its length is 4
```

#### test_01:

```python
longest_subarray_sum([7, 2, 4, 2, 1], 5) # -> -1
```

#### test_02:

```python
longest_subarray_sum([4, 2, 2, 2, 1, 1], 6) # -> 4
```

#### test_03:

```python
longest_subarray_sum([1, 5, 2, 4, 9, 2], 11) # -> 3
```

#### test_04:

```python
longest_subarray_sum([10, 4, 8, 4], 8) # -> 1
```

#### test_05:

```python
longest_subarray_sum([10, 4, 8, 0, 4], 8) # -> 2

```

#### test_06:

```python
longest_subarray_sum([2, 4, 1, 1, 2], 10) # -> 5
```
