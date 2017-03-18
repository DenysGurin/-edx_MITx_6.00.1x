s = 'azcbobobegghakl'

def count_vowels(s):
    total = 0
    vowels = 'aeiou'
    for i in s:
        if i in vowels:
            total += 1
    return total

print count_vowels(s)