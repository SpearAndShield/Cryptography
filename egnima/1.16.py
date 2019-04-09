text="ETEGENLMDNTNEOORDAHATECOESAHLRMT"
ans=""
key=[2,4,6,1,8,3,5,7]
for i in range(0,4):
	for j in range(0,8):
		ans=ans+text[i*8+key[j]-1]
print(ans)