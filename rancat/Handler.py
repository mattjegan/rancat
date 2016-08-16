from io import TextIOWrapper

class Handler(object):
    """
    Provides an interface to interact with
    files, tuples, and lists as per the requirements
    of RanCat.py
    """
    def __init__(self, obj):

        self.raw_obj = obj

        if isinstance(obj, str):
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