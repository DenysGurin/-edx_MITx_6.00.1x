animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    result = 0
    for k in aDict:
        result += len(aDict[k])
    return result

print howMany(animals)
