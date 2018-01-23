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

def getEncodedLetter(matrix, letterRow, letterCol):
    result = matrix[string.ascii_uppercase.index(letterRow)][string.ascii_uppercase.index(letterCol)]

    print('%s x %s -> %s' % (letterRow, letterCol, result))
    return result

def getDecodedLetter(matrix, letterRow, letterCol):
    result = matrix[0][matrix[string.ascii_uppercase.index(letterRow)].index(letterCol)]

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

    result = [getEncodedLetter(matrix, letterKey, letterSource) for letterKey, letterSource in zip(key, source)]

    result = ''.join(result)

    print('done in %s s' % (round(time.time() - start, 5)))

    return result

def decode(source, key):
    source, key = formatInputs(source, key)

    matrix = createMatrix()

    start = time.time()
    print('\nConverting letters...')

    result = [getDecodedLetter(matrix, letterKey, letterSource) for letterKey, letterSource in zip(key, source)]

    result = ''.join(result)

    print('done in %s s' % (round(time.time() - start, 5)))

    return result    
    


if __name__ == '__main__':

    start = time.time()

    source = 'attackatdown'
    key = 'lemon'

    print('Encoding...')

    print('')
    print('Input text: %s' % source)
    print('Key: %s' % key)
    print('')

    enc = encode(source, key)

    print('\n---')
    print('Encoded text is')
    print(enc)
    print('---')

    print('Encoded in %s s\n' % (round(time.time() - start, 5)))

    start_dec = time.time()
    print('***')
    print('Decoding...')

    dec = decode(enc, key)

    print('\n---')
    print('Decoded text is')
    print(dec)
    print('---')
    print('Decoded in %s s\n' % (round(time.time() - start_dec, 5)))


    print('Finished in %s s' % (round(time.time() - start, 5)))