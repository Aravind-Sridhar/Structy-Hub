def longest_word(sentence):
  word = ''

  for words in sentence.split():
    if len(words) >= len(word):
      word = words

  return word