import time

from coder.coder import Coder

if __name__ == '__main__':

    coder = Coder()

    start = time.time()

    source = 'attackatdown'
    key = 'lemon'

    print('Encoding...')

    print('')
    print('Input text: %s' % source)
    print('Key: %s' % key)
    print('')

    enc = coder.encode(source, key)

    print('\n---')
    print('Encoded text is')
    print(enc)
    print('---')

    print('Encoded in %s s\n' % (round(time.time() - start, 5)))

    start_dec = time.time()
    print('***')
    print('Decoding...')

    dec = coder.decode(enc, key)

    print('\n---')
    print('Decoded text is')
    print(dec)
    print('---')
    print('Decoded in %s s\n' % (round(time.time() - start_dec, 5)))


    print('Finished in %s s' % (round(time.time() - start, 5)))