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

def default_conversion(phrase, sep):
    """
    Removes new lines, replaces whitespace and 
    hyphens with sep, removes apostrophies.
    """
    return phrase.rstrip().replace(' ', sep).replace(
            '-', sep).replace('\'', '')

def ascii_lower(phrase, sep):
    phrase = phrase.encode('ascii', 'ignore').lower().decode('utf-8')
    return default_conversion(phrase, sep)

def ascii_upper(phrase, sep):
    phrase = phrase.encode('ascii', 'ignore').upper().decode('utf-8')
    return default_conversion(phrase, sep)

def camel_case(phrase, sep):
    phrase = default_conversion(phrase, sep).lower()
    return phrase[0].upper() + phrase[1:]
