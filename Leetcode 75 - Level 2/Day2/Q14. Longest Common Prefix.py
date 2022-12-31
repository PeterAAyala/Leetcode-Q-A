class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start with flower, check is list[1] = 'flower'
        # if not, flower -> flowe, check again, if not, flowe -> flow
        # repeat until either reach end of list or prefix == ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            match = False
            while not match:
                if prefix == "":
                    break
                if strs[i][:len(prefix)] == prefix:
                    match = True
                else:
                    prefix = prefix[:-1]
        return prefix
                    
                
            
        