def nfruits(dict, str):
    last = 0
    for letter in str:
        last += 1
        for key in dict.keys():
            if letter == key:
                dict[key] -= 1
            elif letter != key and last != len(str):
                dict[key] += 1
    return max(dict.values())

print nfruits({'X': 6, 'K': 7, 'B': 8, 'Z': 8, 'W': 7}, 'ZZBB')