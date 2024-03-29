class Solution(object):
    def wordPattern(self, p, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        words, w_to_p = s.split(' '), dict()
        if len(p)!=len(words):
            return False
        if len(set(p))!=len(set(words)):
            return False
        for i in range(len(words)):
            if words[i] not in w_to_p: 
                w_to_p[words[i]] = p[i]
            elif w_to_p[words[i]] != p[i]: 
                return False

        return True