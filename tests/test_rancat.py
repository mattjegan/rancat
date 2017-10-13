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

import pytest
from rancat import RanCat, conversions

class TestRanCat:
    def test_init_without_seed(self):
        r = RanCat()
        assert len(r.files) == 0
        assert not hasattr(r.seed, '__call__')
        assert hasattr(r._conversion, '__call__')

    def test_init_with_seed(self):
        seed_value = 123
        r = RanCat(seed=seed_value)
        assert len(r.files) == 0
        assert not hasattr(r.seed, '__call__')
        assert r.seed == seed_value
        assert hasattr(r._conversion, '__call__')

    def test_load(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value)
        r.load(datafile)
        assert len(r.files) == 1

    def test_load_url(self):
        data_url = 'http://www.sample-videos.com/text/Sample-text-file-10kb.txt'
        seed_value = 123
        r = RanCat(seed=seed_value)
        r.load(data_url)
        assert len(r.files) == 1
        
    def test_next(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value)
        r.load(datafile)
        value = r.next()
        assert isinstance(value, str)

    def test_open_all(self):
        pass

    def test_default_conversion(self):
        raw_string = 'S\'tr ing   '
        correct_string = 'Str_ing'
        r = RanCat()
        processed_string = r._conversion(raw_string, r._separator)
        assert processed_string == correct_string

    def test_set_conversion(self):
        raw_string = 'string'
        correct_string = raw_string.upper()
        r = RanCat()
        r.set_conversion(str.upper)
        processed_string = r._conversion(raw_string)
        assert processed_string == correct_string

        # Test TypeError gets raised
        with pytest.raises(TypeError):
            r.set_conversion("hello")

    def test_iterable(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value)
        r.load(datafile)
        i = []
        for x in r:
            i.append(x)
            break
        assert i != []

    def test_unique_option(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value)
        r.set_unique(True)
        r.load(datafile)
        i = []
        for x in r:
            i.append(x)
        assert i != []
        assert len(i) == r._total_combinations

    def test_read_size_option(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value)
        r.set_read_size(2)
        r.load(datafile)
        r._refresh_all(r._read_size)
        assert len(r.files[datafile].current_lines) == 2

    def test_duplicate_file_allowed(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value)
        r.load(datafile).load(datafile).load(datafile)
        result = r.next()
        result = result.split('_')
        assert len(result) == 3

    def test_soft_reset(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value, unique=True)
        r.load(datafile).load(datafile)
        i = []
        for x in r:
            i.append(x)
        assert i != []
        assert len(i) == r._total_combinations

        r.soft_reset()
        i = []
        for x in r:
            i.append(x)
        assert i != []
        assert len(i) == r._total_combinations

    def test_hard_reset(self):
        datafile = 'examples/data/colors.txt'
        seed_value = 123
        r = RanCat(seed=seed_value, unique=True)
        r.load(datafile).load(datafile)
        i = []
        for x in r:
            i.append(x)
        assert i != []
        assert len(i) == r._total_combinations

        r = r.hard_reset()
        i = []
        for x in r:
            i.append(x)
        assert i == []
        assert len(r.files) == 0
        assert len(i) == r._total_combinations

    def test_command_chaining(self):
        datafile = 'examples/data/colors.txt'
        r = RanCat().load(datafile).set_unique(True).set_conversion(str.upper).set_read_size(100)
        assert isinstance(r, RanCat)

    def test_load_structure(self):
        datafile = 'examples/data/colors.txt'
        r = RanCat().load_structure(datafile, ['cat', 'dog'])
        phrase = r.next()
        assert phrase.endswith('cat') or phrase.endswith('dog')

    def test_set_separator(self):
        r = RanCat()
        assert r._separator == '_'
        r.set_separator('-')
        assert r._separator == '-'

    def test_default_input(self):
        r = RanCat()
        r.load_default()
        r.load_default()
        assert r.next() != ''


class TestConversions:
    def test_default_conversion(self):
        phrase = conversions.default_conversion('a B-c\'', '_')
        assert phrase == 'a_B_c'

    def test_ascii_lower(self):
        phrase = conversions.ascii_lower('a B-c\'', '_')
        assert phrase == 'a_b_c'

    def test_ascii_upper(self):
        phrase = conversions.ascii_upper('a B-c\'', '_')
        assert phrase == 'A_B_C'

    def test_camel_case(self):
        phrase = conversions.camel_case('a B-c\'', '_')
        assert phrase == 'A_b_c'

def main():
    pass

if __name__ == "__main__": main()
