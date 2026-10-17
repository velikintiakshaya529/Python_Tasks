# Problem 20: Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem


from collections import deque

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        n = int(input())
        cubes = deque(map(int, input().split()))

        previous = float("inf")
        possible = True

        while cubes:
            if cubes[0] >= cubes[-1]:
                current = cubes.popleft()
            else:
                current = cubes.pop()

            if current > previous:
                possible = False
                break

            previous = current

        print("Yes" if possible else "No")
