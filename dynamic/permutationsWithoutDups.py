# 8.7 Cracking the coding int
# Permutations without Dups: Write a method to compute all permutations of a string of unique characters.

class CustomString:
    def __init__(self):
        self.permutationNumer = 0

    def permutations(self, text):
        self.shake(text)
        return self.permutationNumer

    def shake(self, arr):
        if(not arr):
            self.permutationNumer += 1
            return
        for letter in arr:
            arrWithoutEl = list(arr)
            arrWithoutEl.remove(letter)
            self.shake(arrWithoutEl)


print(CustomString().permutations('a'))
print(CustomString().permutations('ab'))
print(CustomString().permutations('abc')) # abc acb bac bca cab cba
print(CustomString().permutations('abcd')) # abc acb bac bca cab cba

