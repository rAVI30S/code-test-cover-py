import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_simple_name(self):
        self.assertEqual(generate_soundex("Robert"), "R163")

    def test_name_with_vowels(self):
        self.assertEqual(generate_soundex("Euler"), "E460")

    def test_name_with_duplicates(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")

    def test_name_with_non_alphabetic(self):
        self.assertEqual(generate_soundex("O'Malley"), "O540")

    def test_name_with_short_length(self):
        self.assertEqual(generate_soundex("Li"), "L000")

    def test_name_with_numbers(self):
        self.assertEqual(generate_soundex("H3llo"), "H040")

    def test_lowercase_name(self):
        self.assertEqual(generate_soundex("example"), "E251")

    def test_mixed_case_name(self):
        self.assertEqual(generate_soundex("McDonald"), "M235")

    def test_name_with_separators(self):
        self.assertEqual(generate_soundex("Hawkins"), "H252")

    def test_name_with_consecutive_h_w(self):
        self.assertEqual(generate_soundex("Bach"), "B200")

    def test_name_with_consecutive_vowels(self):
        self.assertEqual(generate_soundex("Gaia"), "G000")

    def test_name_with_h_w_between_same_digit(self):
        self.assertEqual(generate_soundex("Ruth"), "R300")

    def test_name_with_vowels_and_h_w(self):
        self.assertEqual(generate_soundex("Alvaro"), "A416")

if __name__ == '__main__':
    unittest.main()
