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
