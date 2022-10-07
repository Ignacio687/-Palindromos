class PalindromeWord():
    def palindrome_case(self, word):
        if len(word) == 1:
            return "palindrome"
        else:
            word = word.replace(" ","")
            if word == word[::-1]:
                return "palindrome"

            
