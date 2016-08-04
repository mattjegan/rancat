import random

class RanCat:
    def __init__(self, seed=None, unique=False):
        from collections import OrderedDict
        self.files = OrderedDict()

        from time import time
        self.seed = time() if not seed else seed
        random.seed(self.seed)

        self._conversion = self._default_conversion
        self._unique = unique
        self._total_combinations = 0
        self._seen_map = {}

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()

    def next(self):
        self._open_all()

        if len(self._seen_map.keys()) == self._total_combinations:
            raise StopIteration('Exhausted combinations')

        # Build the string
        seen = False
        while not seen:
            result_string = ''
            for f in self.files.values():    
                choice = random.choice(f)
                result_string += self._conversion(choice) + '_'
            result_string = result_string[:-1]

            if not self._unique:
                return result_string

            if not self._seen_map.get(result_string, False):
                self._seen_map[result_string] = True
                seen = True

        return result_string

    def load(self, filepath):
        """
        TODO: Make this a lazy load
        """
        self.files[filepath] = [line for line in open(filepath, 'r')]
        if self._total_combinations != 0:
            self._total_combinations *= len(self.files[filepath])
        else:
            self._total_combinations = len(self.files[filepath])

    def _open_all(self):
        """
        Opens all the files

        TODO: Implement when doing lazy loading
        """
        return

    def _default_conversion(self, phrase):
        """
        Removes new lines, replaces whitespace and 
        hyphens with underscores, removes apostrophies.
        """
        return phrase.rstrip().replace(' ', '_').replace(
            '-', '_').replace('\'', '')

    def set_conversion(self, conversion_callable):
        """
        Sets the conversion method for phrases
        """
        if hasattr(conversion_callable, '__call__'):
            self._conversion = conversion_callable
        else:
            raise TypeError('{} must be callable'.format(str(conversion_callable)))

    def set_unique(self, boolean):
        self._unique = bool(boolean)