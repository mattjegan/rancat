"""
Copyright 2016 Matthew Egan

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from collections import OrderedDict
import random
import os

from .conversions import default_conversion
from .Handler import Handler


class RanCat(object):
    def __init__(self, seed=None, unique=False, read_size=1000):
        self.files = OrderedDict()

        from time import time
        self.seed = time() if not seed else seed
        random.seed(self.seed)

        self._conversion = default_conversion
        self._separator = '_'
        self._unique = bool(unique)
        self._total_combinations = 0
        self._seen_map = {}
        self._read_size = int(read_size)
        self._assets_path = os.path.dirname(os.path.realpath(__file__)) \
                + os.path.sep + "assets" + os.path.sep

    def __del__(self):
        for filepath in self.files:
            self.files[filepath].close()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if (len(self._seen_map.keys()) < self._total_combinations and \
            len(self._seen_map.keys()) > self._total_combinations // 2) \
            or len(self._seen_map.keys()) == 0:
            self._refresh_all(self._read_size)

        if len(self._seen_map.keys()) == self._total_combinations:
            raise StopIteration('Exhausted combinations')

        # Build the string
        seen = False
        while not seen:
            result_string = ''
            for file_tuple in self.files.values():
                choice = random.choice(file_tuple.current_lines)
                result_string += self._conversion(choice, self._separator) + self._separator
            result_string = result_string[:-1]

            if not self._unique:
                return result_string

            if not self._seen_map.get(result_string, False):
                self._seen_map[result_string] = True
                seen = True

        return result_string

    def load(self, filepath):

        original_filepath = filepath
        filepath = str(filepath)
        while filepath in self.files:
            # We can multi-hash here since we don't need
            # to be able to access a file via filepath after this
            # method.
            filepath = hash(filepath) * hash(filepath)

        self.files[filepath] = Handler(original_filepath)

        return self

    def soft_reset(self):
        """
        Resets the combination tracking
        """
        self._total_combinations = 0
        self._seen_map = {}
        return self

    def hard_reset(self):
        """
        Performs a soft reset as well as clears the files structure
        """
        self.soft_reset()
        for filepath in self.files:
            self.files[filepath].close()
        self.files = OrderedDict()
        return self

    def _refresh_all(self, n):
        """
        Reads in the next n lines from the files
        """
        self._total_combinations = 0
        for filepath in self.files:
            if self.files[filepath].is_open():
                for _ in range(0, n):
                    line = self.files[filepath].read_next()
                    if not line:
                        self.files[filepath].close()
                        break
                    self.files[filepath].append(line)

            # Recalculate _total_combinations
            if self._total_combinations == 0:
                self._total_combinations = len(self.files[filepath].current_lines)
            else:
                self._total_combinations *= len(self.files[filepath].current_lines)

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

    def set_separator(self, sep):
        self._separator = str(sep)
        return self

    def load_structure(self, *args):
        """
        Accepts a number of arguments which may be filepaths
        or lists/tuples.

        If the arg was a filepath then it is loaded, otherwise
        the list/tuple is used like a file.
        """
        for obj in args:
            self.load(obj)

        return self

    def load_default(self):
        """
        Loads the lorem ipsum text from assets/lorem_ipsum.txt
        """
        self.load(self._assets_path + "lorem_ipsum.txt")
