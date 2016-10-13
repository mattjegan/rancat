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
    return default_conversion(phrase.encode('ascii', 'ignore').decode('utf-8').lower(), sep)

def ascii_upper(phrase, sep):
    return default_conversion(phrase.encode('ascii', 'ignore').decode('utf-8').upper(), sep)

def camel_case(phrase, sep):
    phrase = default_conversion(phrase, sep).lower()
    return phrase[0].upper() + phrase[1:]

def tech_conversion(text):
	"""
	If a global variable (TODO: create global variable) is set to true
	run final contatination through this function.
	"""

	#These could be done in a txt file faster probably.
	hackStarts = ['H','K','C','T','P','J','W','F']
	hackEnds = ['ACK','AK','AWK','OC','OK','ICK','AX','ECK','IT','OCK','AP','ALK']
	hacklist = []

	for start in hackStarts:
		for end in hackEnds:
			hacklist.append('%s%s' % (start, end)) #generate substrings to be replaced.

	#randomize order or list. Not sure how to do this.

	for sub in hacklist:
		if(sub in text):
			text.replace(sub, "hack", 1)
			return text#just replace hack once.

	return text
