class Solution:

    def __init__(self):
        # Dictionary of substrings that work
        self.dct = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Idea: Recursion with a cache
        # For each word in wordDict-> if it prefixes s, recurse with the substring & cache any substring that works

        if s in self.dct:
            return self.dct[s]
        elif s=="":
            return True

        for prefix in wordDict:
            
            # Check if we have a prefix to space-seperate our string with
            if s.startswith(prefix):
                
                # recurse with the suffix-substring
                canSegment = self.wordBreak(s.removeprefix(prefix) , wordDict) # {prefix}{suffix} -> just pass the suffix
                if canSegment:
                    self.dct[s] = True
                    return True

        self.dct[s] = False
        return False