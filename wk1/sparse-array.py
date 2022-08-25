
def matchingStrings(strings, queries):
    instances = [0] * len(queries)

    for i in range(len(queries)):
        query = queries[i]

        for string in strings:
            if query == string:
                instances[i] += 1

    print(*instances, sep='\n')
    return instances


strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
matchingStrings(strings, queries)
