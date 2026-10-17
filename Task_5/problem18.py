# Problem 18: The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    vowels = "AEIOU"
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")


if __name__ == "__main__":
    s = input().strip()
    minion_game(s)
