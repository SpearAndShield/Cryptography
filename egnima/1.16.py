text="ETEGENLMDNTNEOORDAHATECOESAHLRMI"
ans=""
key=[4,1,6,2,7,3,8,5]
for i in range(0,4):
	for j in range(0,8):
		ans=ans+text[i*8+key[j]-1]
print(ans)