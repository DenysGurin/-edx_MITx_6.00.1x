animals = ({'a': [13, 0, 6, 6, 6, 12, 13, 5, 16, 20], 'c': [17, 9, 0, 19, 8, 10, 20], 'b': [], 'e': [7, 18, 10, 4], 'd': [19, 13, 9]})
empty = {}

def biggest(aDict):
    if aDict == {}:
        return None
    else:
        for key in aDict.keys():
            #print key, aDict[key]
            aDict[key] = sum(aDict[key])
            #print key, aDict[key]
        for key in aDict.keys():
            #print key, aDict[key], aDict.values()
            if aDict[key] == max(aDict.values()):
                return key

print biggest(animals)
print biggest(empty)