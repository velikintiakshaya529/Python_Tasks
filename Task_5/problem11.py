# Problem 11: Text Wrap
# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == "__main__":
    string = input("Enter a string: ")
    max_width = int(input("Enter the width: "))
    result = wrap(string, max_width)
    print(result)
