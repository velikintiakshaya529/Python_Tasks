# Problem 1: Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input("Enter the number of scores: "))
scores = list(map(int, input("Enter the scores: ").split()))

unique_scores = sorted(set(scores))

print(unique_scores[-2])