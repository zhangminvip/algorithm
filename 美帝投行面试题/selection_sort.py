# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:57:22 2017

@author: zhangmin
"""

def longestChain(words):
    max_len = 0
    wd = {}
    
    for w in words:
#        print(w)
        wd[w] = 1
    print(wd)
        
    words.sort(key=lambda x:len(x))
    
    print(words)
    
    x = 0
#    print(words)
    for word in words:
        for i in range(len(word)):
            
#            print(wd[word])
            
            subword = word[:i] +word[i + 1:]
            
            print(x,subword)
            
        
#            print(word[:i],'\n')
            x = x+1
            if subword in wd:
                
                print('yes')
                wd[word] = max(wd[word], wd[subword] + 1)
                
        max_len = max(max_len, wd[word])
        
    return max_len

words = ['6', 'a', 'b', 'ba' ,'bca' , 'bda' ,'bdca']

print(longestChain(words))
            
    