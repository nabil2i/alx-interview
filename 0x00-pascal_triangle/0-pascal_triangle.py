#!/usr/bin/python3
""" Module of function pascal_triangle"""


def pascal_triangle(n):
  """function returns a list of integers
  representing the Pascal's triangle of n
  """
  myList = []
  mySubList = []
  if (n <= 0):
    return myList
  for i in range(n):
    mySubList = [1]
    if myList:
      lastList = myList[-1]
      mySubList.extend([sum(pair) for pair in zip(lastList, lastList[1:])])
      mySubList.append(1)
    myList.append(mySubList)
  return (myList)
