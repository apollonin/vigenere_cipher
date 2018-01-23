import string
import time
import math

def createMatrix():
    start = time.time()
    print('\nGenerating matrix...', end='')
    
    l = len(string.ascii_uppercase)

    matrix = [[(string.ascii_uppercase*2)[i+j] for i in range(l)] for j in range(l)]

    print('done in %s s' % (round(time.time() - start, 5)))

    return matrix

def getMartixIntersection(matrix, letterRow, letterCol):
    result = matrix[string.ascii_uppercase.index(letterRow)][string.ascii_uppercase.index(letterCol)]

    print('%s x %s -> %s' % (letterRow, letterCol, result))
    return result

def formatInputs(source, key):
    print('\nPreparing source and key data...')
    source = source.upper()
    key = (key * math.ceil(len(source)/len(key)))[:len(source)].upper()

    print('Source is now: %s' % source)
    print('Key is now:    %s' % key)

    return source, key

def encode(source, key):
    source, key = formatInputs(source, key)

    matrix = createMatrix()

    start = time.time()
    print('\nConverting letters...')

    result = [getMartixIntersection(matrix, letterKey, letterSource) for letterKey, letterSource in zip(key, source)]

    result = ''.join(result)

    print('done in %s s' % (round(time.time() - start, 5)))

    return result
    


if __name__ == '__main__':

    start = time.time()

    source = 'attackatdown'
    key = 'lemon'

    print('Start...')

    print('')
    print('Input text: %s' % source)
    print('Key: %s' % key)
    print('')

    result = encode(source, key)

    print('\n---')
    print('Encoded text is')
    print(result)
    print('---')


    print('Finished in %s s' % (round(time.time() - start, 5)))