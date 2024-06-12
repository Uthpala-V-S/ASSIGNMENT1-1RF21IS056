def get_possibilities(s):
    if len(s) == 1:
        return [s]
    possibilities = []
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        for p in get_possibilities(remaining_str):
            possibilities.append(char + p)
    return possibilities

s = input("Enter a string: ")
print("All possibilities of the string are: ", get_possibilities(s))