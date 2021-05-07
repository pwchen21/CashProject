class Solution:
	def letterCasePermutation(self, S):
		res = ['']
		for ch in S:
		    if ch.isalpha():
		        res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
		    else:
		        res = [i+ch for i in res]
		    print(res)
		return res



A=Solution()
A.letterCasePermutation('aba')
print('================')
A.letterCasePermutation('0')
