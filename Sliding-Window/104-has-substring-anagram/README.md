## has substring anagram

Write a function that takes in a string and an anagram. The function should return a boolean indicating whether or not
the string contains a substring with the same characters as the anagram.

You can assume that the string contains no duplicate characters.

You can assume that the anagram contains no duplicate characters.

You can assume that the anagram is not longer than the string.

#### test_00:

```python
has_substring_anagram("greyhounds", "hoy") # -> True
# the substring "yho" is an anagram of "hoy"
```

#### test_01:

```python
has_substring_anagram("gruyheonds", "hoy") # -> False
```

#### test_02:

```python
has_substring_anagram("breakdowns", "snow") # -> True
```

#### test_03:

```python
has_substring_anagram("dermatoglyphics", "red") # -> True
```

#### test_04:

```python
has_substring_anagram("southernly", "thorny") # -> false
```

#### test_05:

```python
has_substring_anagram("southernly", "nerlysouth") # -> true
```
