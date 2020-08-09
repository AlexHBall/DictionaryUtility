import unittest
import json

from dictionary_entry import Dictonary_Entry

class TestDictionaryEntry(unittest.TestCase):
    def test_pronounciation(self):
        j = json.dumps({'name' : 'être', 'pronounciation': "ê-tr'"})
        entry = Dictonary_Entry("être")
        self.assertEqual(j, entry.get_pronounciation())
if __name__ == '__main__':
    unittest.main()