# get_fullname.py

def get_formatted_fullname(first_name, last_name, middle_name=''):
    """Generate a neatly formatted full name."""
    if middle_name:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

