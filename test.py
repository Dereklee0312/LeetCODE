s= "MCMXCIV"
romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

total = 0
skip = None

for index, char in enumerate(s[::-1]):
    if (romans[s[len(s) - index - 2]] < romans[char]) and (index != len(s) - 1):
        total -= romans[s[len(s) - index - 2]]
        skip = len(s) - index - 2
    if skip == None:
        total += romans[char]
    elif index != len(s)-skip-1:
        total += romans[char]

print(total)
