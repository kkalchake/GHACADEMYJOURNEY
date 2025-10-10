#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Solving engineer: Kamila Kalchakeeva
# https://github.com/kkalchake

# When A. match_ends is called:
# req 1) from list [words] returns the count of the number of strings
# req 2) the length of string should be 
#          a) 2 or more AND
#          b) first and last chars of string are the same 

def match_ends(words):
  count = 0
  for string in (words):
    if len(string) >= 2 and string[0] == string[-1]:
      count +=1 
  return count

# When B. front_x is called:
# req 1) returns sorted list from given [words] list in below order
#        a) first group sorted list of strings start with 'x' concat WITH
#        b) second sorted list with the rest strings

def front_x(words):
  list_with_x = []
  list_without_x = []
  for string in words:
    if string.startswith("x"):
      list_with_x.append(string)
    else:
      list_without_x.append(string)
  
  sorted_list = sorted(list_with_x) + sorted(list_without_x)
  return sorted_list

# When C. sort_last is called:
# req 1) returns sorted in increasing order list from given non-empty tuple 
#        a) the order is steered by the last element in each tuple

def sort_last(tuples):
    def last_elem(t):
        return t[-1]
    return sorted(tuples, key=last_elem)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print()
  print('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


  print()
  print('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()