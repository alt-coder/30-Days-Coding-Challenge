'''
## Problem statement
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]'''

'''
## Link 
https://leetcode.com/problems/group-anagrams/
# '''

from collections import Counter, defaultdict

'''
## how i approched the problem 
for every string 
map[sorted(string)].append(string)
so we have sorted sequence of string as key and value as the list of string that has the same sorted sequence
The total time complexity of the program will be  O(n*klogk)
'''


'''
key idea is to create a hasing function that can hash any string
 depending upon charaters and number of times a charater is repeated.
 Such as this example 'feet' can be hashed to 2e1f1t [notice the charaters are in ascending order with their frequncy ]
 therefore 'teef' will also hash to '2e1f1t' .
 Now for every string in the array generate the hash and keep that hash as key and values as the list of string
 that has mapped to same hash.
If hashing takes constent time then the time complexity is O(n)
'''
class Solution:
    def genhash(self,string):
        counter = Counter(string)
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        hash=''
        for char in alphabets:
            if char in counter:
                hash+=(str(counter[char])+char)
        return hash

     
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = defaultdict(list)
        for st in strs:
            ls[self.genhash(st)].append(st)
        return ls.values()
