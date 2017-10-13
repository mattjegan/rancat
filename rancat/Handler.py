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

from io import TextIOWrapper
from urllib.parse import urlparse
import requests

class Handler(object):
    """
    Provides an interface to interact with
    files, tuples, and lists as per the requirements
    of RanCat.py
    """
    def __init__(self, obj):

        self.raw_obj = obj

        if isinstance(obj, str) and urlparse(obj).scheme :
            self.obj_type = list
            self.page = requests.get(obj)
            self.processed_obj = [line.decode('utf8') for line in self.page]
            self.current_lines = [line.decode('utf8') for line in self.page]
            self.opened = True
            self.cursor = 0

        elif isinstance(obj, str):
            self.obj_type = TextIOWrapper
            self.processed_obj = open(obj, 'r')
            self.current_lines = []
            self.opened = True

        elif isinstance(obj, list) or isinstance(obj, tuple):
            self.obj_type = list
            self.processed_obj = list(obj)
            self.current_lines = list(obj)
            self.opened = True
            self.cursor = 0

    def close(self):
        if self.obj_type == TextIOWrapper:
            self.processed_obj.close()
        self.opened = False

    def read_next(self):
        if self.obj_type == TextIOWrapper:
            return self.processed_obj.readline()
        else:
            self.cursor += 1
            if self.cursor >= len(self.processed_obj):
                return ''
            return self.processed_obj[self.cursor]

    def is_open(self):
        return self.opened

    def append(self, data):
        self.current_lines.append(data)
        return self