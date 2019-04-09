text="MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW!!!!!!"
ans=""
m,n=4,3
for i in range(0,4):
	for j in range(0,n):
		for k in range(0,m):
			if text[i*m*n+j+k*n]!="!":
				print(text[i*m*n+j+k*n])
				ans=ans+text[i*m*n+j+k*n]
print(ans)
'''m=[2,3,6,7,14,21]
n=[21,14,7,6,3,2]
for i in range(0,6):
	ans=""
	for j in range(0,n[i]):
		for k in range(0,m[i]):
			ans=ans+text[j+k*n[i]]
	print(ans)'''
	