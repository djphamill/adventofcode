# Commonly used functions

def get_list_from_file(filepath, sep='\n'):
    """
    Return a list from a file
    """
    with open(filepath, 'r') as f:
        l = f.read().split(sep)
    
    return l

