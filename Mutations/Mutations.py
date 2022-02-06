# Question Link:- https://www.hackerrank.com/challenges/python-mutations/problem #
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:] #slicing the string and concatenating to return a new string
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
