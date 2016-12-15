class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomLetters = {}
        for i in magazine:
            try:
                ransomLetters[i] += 1
            except:
                ransomLetters[i] = 1
        for i in ransomNote:
            try:
                if ransomLetters[i] == 0:
                    return False
                else:
                    ransomLetters[i] -= 1
            except:
                return False
        return True
        
