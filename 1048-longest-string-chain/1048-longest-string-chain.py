import math
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # maxCount = 0
        # currHM = dict([])
        # maxLen = 0
        # minLen = math.inf
        # maxLost = {}
        # lastLost = False
        # lost = 0
        # for word in range(len(words)-1,-1,-1):
        #     currWord = words[word]
        #     currLen = len(words[word])
        #     if(maxLen<currLen):
        #             maxLen = currLen
        #     if(minLen>currLen):
        #             minLen = currLen
        #     if(currHM.get(currLen) is not None):
        #         currHM[currLen].append(currWord)
        #     else:
        #         currHM[currLen] = [currWord]
        # currLen = maxLen
        # while(currLen>=minLen+1):
        #     # ourWord = ""
        #     found = False
        #     if(currHM.get(currLen) is not None):
        #         for word in currHM[currLen]:
        #             skip = 0 
        #             while(skip<=currLen):
        #                 # print(currHM[currLen],word[:skip]+word[skip+1:])
        #                 if(currHM.get(currLen-1) is None):
        #                     found = True
        #                     break;
        #                 if(word[:skip]+word[skip+1:] in currHM[currLen-1]):
        #                     maxCount+=1
        #                     found = True
        #                     break;
        #                 skip+=1
        #             if(found==True):
        #                 break;
        #         currLen-=1
        #     else:
        #         currLen-=1
        #         lastLost = True
        # if(maxCount+1-lost<=0):
        #     return 1
        # return maxCount+1-lost
        
        dp = {}
        
        words = sorted(words, key = len)
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                toSearch = word[:i]+word[i+1:]
                dp[word] = max(dp.get(toSearch,0)+1,dp[word])
        return max(dp.values())
            
                    
            