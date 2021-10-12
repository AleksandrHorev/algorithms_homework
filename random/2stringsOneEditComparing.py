# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
#  pale, bale -> true
#   pale, bake -> false

class StringComparing:
    def compare(self, first, second):
        countEdits = i = j = 0
        movedPointer = False
        firstLen = len(first)
        secondLen = len(second)
        if (abs(firstLen - secondLen) > 1): return False

        while i < firstLen and j < secondLen:
            if (countEdits > 1): return False

            if (first[i] == second[j]):
                i += 1
                j += 1
                continue

            if (i + 1 < firstLen and first[i + 1] == second[j]):
                i += 2
                j += 1
                movedPointer = True
                continue

            if (j + 1 < secondLen and first[i] == second[j + 1]):
                i += 1
                j += 2
                movedPointer = True
                continue

            countEdits += 1
            i += 1
            j += 1
              
              # add check on whhat the type the error was ?
        if (countEdits > 1 or
           (movedPointer and i != firstLen) or
           (movedPointer and j != secondLen) or
           ((i != firstLen or j != secondLen) and countEdits == 1)):
            return False
        return True

print(StringComparing().compare('pale', 'pale'))   # true
print(StringComparing().compare('pale', 'pole'))   #  true
print(StringComparing().compare('pokle', 'pole'))  # true
print(StringComparing().compare('pale', 'padle'))  # true
print(StringComparing().compare('pol', 'pole'))    # true
print(StringComparing().compare('pol', 'polee'))    # false
print(StringComparing().compare('ole', 'pole'))    # true
print(StringComparing().compare('ple', 'pole'))    # true
print(StringComparing().compare('pale', 'poles'))  # false