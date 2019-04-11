import itertools
text="MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW"
'''m=[2,3,6,7,14,21]
n=[21,14,7,6,3,2]
def getList(x):
	com_num=[]
	for i in range(0,x):
		com_num.append(i)
	return (list(itertools.permutations(com_num, x)))
for i in range(0,6):
	for k in getList(m[i]):
		ans=""
		for j in range(0,n[i]):
			for t in k:
				ans=ans+text[t+j*m[i]]
		print("m="+str(m[i])+" , "+"n="+str(n[i])+" : ")
		print(ans)'''
	
# m=6,n=7,key=(1,3,5,2,4,6)
ans=""
for i in range(0,7):
	for t in (0,2,4,1,3,5):
		ans=ans+text[t+i*6]
print (ans)
	