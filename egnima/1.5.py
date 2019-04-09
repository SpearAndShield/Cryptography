text="BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
key=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(1,26):
	ans=""
	for j in range(0,len(text)):
		ans=ans+key[(key.index(text[j])+i)%26]
	print(ans)
	
