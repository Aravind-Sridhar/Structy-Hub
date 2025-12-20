def longest_word(sentence):
  max_len = -float('inf')
  max_word = ''

  for word in sentence.split():
    curr_len = len(word)
    if curr_len >= max_len:
      max_len = curr_len
      max_word = word

  return max_word