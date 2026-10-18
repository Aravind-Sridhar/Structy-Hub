def reverse_string(s):
  if not s:
    return ''
  return s[-1] + reverse_string(s[-2:])