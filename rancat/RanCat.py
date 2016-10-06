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

from .conversions import default_conversion
from .Handler import Handler

class RanCat(object):
    def __init__(self, seed=None, unique=False, read_size=1000):
        self.handlers = OrderedDict()

        from time import time
        self.seed = time() if not seed else seed
        random.seed(self.seed)

        self._conversion = default_conversion
        self._separator = '_'
        self._unique = bool(unique)
        self._total_combinations = 0
        self._seen_map = {}
        self._read_size = int(read_size)

    def __del__(self):
        for handler in self.handlers:
            self.handlers[handler].close()

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
            for handler in self.handlers.values():
                choice = random.choice(handler.current_lines)
                result_string += self._conversion(choice, self._separator) + self._separator
            result_string = result_string[:-1]

            if not self._unique:
                return result_string

            if not self._seen_map.get(result_string, False):
                self._seen_map[result_string] = True
                seen = True

        return result_string

    def load(self, *sources):
        """
        Initialize Handler instances using sources and add to handlers list
        """
        for source in sources:
            original_source = source
            source = str(source)
            while source in self.handlers:
                # We can multi-hash here since we don't need
                # to be able to access a file via filepath after this
                # method.
                source = hash(source) * hash(source)

            self.handlers[source] = Handler(original_source)

        return self

    def soft_reset(self):
        """
        Reset the combination tracking
        """
        self._total_combinations = 0
        self._seen_map = {}
        return self

    def hard_reset(self):
        """
        Perform a soft reset as well as clear the files structure
        """
        self.soft_reset()
        for handler in self.handlers:
            self.handlers[handler].close()
        self.handlers = OrderedDict()
        return self

    def _refresh_all(self, n):
        """
        Read in the next n lines from handlers
        """
        self._total_combinations = 0
        for handler in self.handlers:
            if self.handlers[handler].is_open():
                for _ in range(0, n):
                    line = self.handlers[handler].read_next()
                    if not line:
                        self.handlers[handler].close()
                        break
                    self.handlers[handler].append(line)

            # Recalculate _total_combinations
            if self._total_combinations == 0:
                self._total_combinations = len(self.handlers[handler].current_lines)
            else:
                self._total_combinations *= len(self.handlers[handler].current_lines)

    def set_conversion(self, conversion_callable):
        """
        Set the conversion method for phrases
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
