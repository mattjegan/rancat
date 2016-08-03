import random

class RanCat:
    def __init__(self, seed=None):
        from collections import OrderedDict
        self.files = OrderedDict()

        from time import time
        self.seed = time if not seed else seed
        random.seed(self.seed)

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
            result_string += self._tokenize(choice) + '_'
        return result_string[:-1]

    def _open_all(self):
        """
        Opens all the files

        TODO: Implement when doing lazy loading
        """
        return

    def _tokenize(self, phrase):
        """
        Removes new lines, replaces whitespace and 
        hyphens with underscores, removes apostrophies.
        """
        return phrase.strip('\n').replace(' ', '_').replace(
            '-', '_').replace('\'', '')
