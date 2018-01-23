import time
import string

def create():
    start = time.time()
    print('\nGenerating matrix...', end='')
    
    l = len(string.ascii_uppercase)

    matrix = [[(string.ascii_uppercase*2)[i+j] for i in range(l)] for j in range(l)]

    print('done in %s s' % (round(time.time() - start, 5)))

    return matrix

def encode_letter(matrix, letterRow, letterCol):
    result = matrix[string.ascii_uppercase.index(letterRow)][string.ascii_uppercase.index(letterCol)]

    print('%s x %s -> %s' % (letterRow, letterCol, result))
    return result

def decode_letter(matrix, letterRow, letterCol):
    result = matrix[0][matrix[string.ascii_uppercase.index(letterRow)].index(letterCol)]

    print('%s x %s -> %s' % (letterRow, letterCol, result))
    return result