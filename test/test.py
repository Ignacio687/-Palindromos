import unittest
from main.classpalindrome import PalindromeWord
word = PalindromeWord()

class Palindromo_TestCase(unittest.TestCase):
    def test_1case(self):
        self.assertEqual(word.palindrome_case("a"), "palindrome")
    def test_2case(self):
        self.assertEqual(word.palindrome_case("ana"), "palindrome")
    def test_3case(self):
        self.assertEqual(word.palindrome_case("an a"), "palindrome")
    def test_4case(self):
        self.assertEqual(word.palindrome_case("arenera"), "palindrome")
    def test_5case(self):
        self.assertEqual(word.palindrome_case("oso"), "palindrome")
    def test_6case(self):
        self.assertEqual(word.palindrome_case("ojo"), "palindrome")
    def test_7case(self):
        self.assertEqual(word.palindrome_case("o j o"), "palindrome")

# if __name__=="__main__":
#     unittest.main()