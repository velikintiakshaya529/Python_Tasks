# Problem 3: Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == "__main__":
    s = input("Enter the string: ")
    i = int(input("Enter the position: "))
    c = input("Enter the replacement character: ")
    result = mutate_string(s, i, c)
    print(result)
