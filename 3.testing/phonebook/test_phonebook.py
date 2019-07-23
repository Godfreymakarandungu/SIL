import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        
    def test_lookup_entry_by_name(self):
        phonebook = Phonebook()
        phonebook.add('Bob', '12345')
        self.assertEqual("12345", phonebook.lookup("Bob"))

    def test_missing_entry_raises_KeyError(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")
        self.assertTrue(self.phonebook.is_consistent())
