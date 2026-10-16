def pair_sum(numbers, target_sum):
  dict ={}

  for i in range(len(numbers)):
    if target_sum - numbers[i] in dict:
      return (i, dict[target_sum - numbers[i]])
    dict[numbers[i]] = i
