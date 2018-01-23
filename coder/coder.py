import math
import time

from tabula_recta import tabula_recta

class Coder(object):

    def encode(self, source, key):
        source, key = self._formatInputs(source, key)

        matrix = tabula_recta.create()

        start = time.time()
        print('\nConverting letters...')

        result = [tabula_recta.encode_letter(matrix, letterKey, letterSource) for letterKey, letterSource in zip(key, source)]

        result = ''.join(result)

        print('done in %s s' % (round(time.time() - start, 5)))

        return result

    def decode(self, source, key):
        source, key = self._formatInputs(source, key)

        matrix = tabula_recta.create()

        start = time.time()
        print('\nConverting letters...')

        result = [tabula_recta.decode_letter(matrix, letterKey, letterSource) for letterKey, letterSource in zip(key, source)]

        result = ''.join(result)

        print('done in %s s' % (round(time.time() - start, 5)))

        return result    

    def _formatInputs(self, source, key):
        print('\nPreparing source and key data...')
        source = source.upper()
        key = (key * math.ceil(len(source)/len(key)))[:len(source)].upper()

        print('Source is now: %s' % source)
        print('Key is now:    %s' % key)

        return source, key