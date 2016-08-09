import random

class RanCat:
    def __init__(self, seed=None, unique=False, read_size=1000):
        from collections import OrderedDict
        self.files = OrderedDict()

        from time import time
        self.seed = time() if not seed else seed
        random.seed(self.seed)

        self._conversion = self._default_conversion
        self._unique = bool(unique)
        self._total_combinations = 0
        self._seen_map = {}
        self._read_size = int(read_size)

    def __del__(self):
        for filepath in self.files:
            try:
                self.files[filepath][0].close()
            except:
                continue

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()

    def next(self):
        if (len(self._seen_map.keys()) < self._total_combinations and len(self._seen_map.keys()) > self._total_combinations // 2) or len(self._seen_map.keys()) == 0:
            self._refresh_all(self._read_size)

        if len(self._seen_map.keys()) == self._total_combinations:
            raise StopIteration('Exhausted combinations')

        # Build the string
        seen = False
        while not seen:
            result_string = ''
            for file_tuple in self.files.values():    
                choice = random.choice(file_tuple[1])
                result_string += self._conversion(choice) + '_'
            result_string = result_string[:-1]

            if not self._unique:
                return result_string

            if not self._seen_map.get(result_string, False):
                self._seen_map[result_string] = True
                seen = True

        return result_string

    def load(self, filepath):
        self.files[filepath] = [open(filepath, 'r'), [], True] # (file_obj, current_lines, open)
        return self

    def _open_all(self):
        """
        Opens all the files

        TODO: Implement when doing lazy loading
        """
        return

    def _refresh_all(self, n):
        """
        Reads in the next n lines from the files
        """
        self._total_combinations = 0
        for filepath in self.files:
            if self.files[filepath][2]:
                for i in range(0, n):
                    line = self.files[filepath][0].readline()
                    if not line:
                        self.files[filepath][0].close()
                        self.files[filepath][2] = False
                        break
                    self.files[filepath][1].append(line)

            # Recalculate _total_combinations
            if self._total_combinations == 0:
                self._total_combinations = len(self.files[filepath][1])
            else:
                self._total_combinations *= len(self.files[filepath][1])

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
        return self

    def set_unique(self, boolean):
        self._unique = bool(boolean)
        return self

    def set_read_size(self, read_size):
        self._read_size = int(read_size)
        return self
        