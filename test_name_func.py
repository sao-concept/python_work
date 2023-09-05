import unittest
from name import get_formatted_fullname

class NamesTestCase(unittest.TestCase):
    """Tests for 'name.py'."""
 
def test_first_last_name(self):
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_fullname('azeez', 'saka')
    self.assertEqual(formatted_name, 'Azeez Saka')

def test_first_last_middle_name(self):
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('azeez', 'olamilekan', 'saka')
    self.assertEqual(formatted_name, 'Azeez Olamilekan Saka')

unittest.main()
