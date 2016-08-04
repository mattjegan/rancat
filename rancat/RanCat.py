import random

class RanCat:
    def __init__(self, seed=None):
        from collections import OrderedDict
        self.files = OrderedDict()

        from time import time
        self.seed = time() if not seed else seed
        random.seed(self.seed)

        self._conversion = self._default_conversion

    def load(self, filepath):
        """
        TODO: Make this a lazy load
        """
        self.files[filepath] = [line for line in open(filepath, 'r')]

    def next(self):
        """
        TODO: Convert this class to a proper iterator
        """
        self._open_all()

        # Build the string
        result_string = ''
        for f in self.files.values():
            choice = random.choice(f)
            result_string += self._conversion(choice) + '_'
        return result_string[:-1]

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
