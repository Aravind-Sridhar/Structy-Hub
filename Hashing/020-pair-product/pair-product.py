def pair_product(numbers, target_product):
  result = {}

  for idx, num in enumerate(numbers):
    div = target_product / num

    if 