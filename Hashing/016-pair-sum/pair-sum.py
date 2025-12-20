def pair_sum(numbers, target_sum):
  dict = {}

  for i in range(len(numbers)):
    diff = target_sum - numbers[i]

    if diff in dict:
      return i, dict[diff]

    dict[numbers[i]] = i