def pair_product(numbers, target_product):
  dict = {}

  for i in range(len(numbers)):
    rem = target_product/numbers[i]

    if rem in dict:
      return i, dict[rem]

    dict[numbers[i]] = i
    