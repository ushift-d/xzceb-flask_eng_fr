import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test_null(self):
        self.assertEqual(english_to_french(''), None)
        self.assertIsNone(english_to_french(), 'Value is not null or none')

    def test_translate(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('yes'), 'non')
   

class Testfrench_to_english(unittest.TestCase):
    def test_null(self):
        self.assertEqual(french_to_english(''), None)
        self.assertIsNone(french_to_english(), 'Value is not null or none')
    def test_translate(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Quel travail difficile'), 'really easy')
   
unittest.main()
