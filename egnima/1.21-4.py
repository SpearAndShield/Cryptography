text="BNVSNSIHQCEELSSKKYERIFJKXUMBGYKAMQLJTYAVFBKVTDVBPVVRJYYLAOKYMPQSCGDLFSRLLPROYGESEBUUALRWXMMASAZLGLEDFJBZAVVPXWICGJXASCBYEHOSNMULKCEAHTQOKMFLEBKFXLRRFDTZXCIWBJSICBGAWDVYDHAVFJXZIBKCGJIWEAHTTOEWTUHKRQVVRGZBXYIREMMASCSPBHLHJMBLRFFJELHWEYLWISTFVVYEJCMHYUYRUFSFMGESIGRLWALSWMNUHSIMYYITCCQPZSICEHBCCMZFEGVJYOCDEMMPGHVAAUMELCMOEHVLTIPSUYILVGFLMVWDVYDBTHFRAYISYSGKVSUUHYHGGCKTMBLRX"
alphebat={'A':0.08167,'B':0.01492,'C':0.02782,'D':0.04253,
'E':0.12702,'F':0.02228,'G':0.02015,'H':0.06094,'I':0.06966,
'J':0.00153,'K':0.100772,'L':0.04025,'M':0.02406,'N':0.06749,
'O':0.07507,'P':0.01929,'Q':0.00095,'R':0.05987,'S':0.06327,
'T':0.09056,'U':0.02758,'V':0.00978,'W':0.02360,'X':0.00150,
'Y':0.01974,'Z':0.00074}
def calculate(x):
	length=len(x)
	dict={}
	for i in x:
		if i in dict:
			dict[i]=dict[i]+1
		else:
			dict[i]=1
	'''M=[]
	step,min=0,100
	for i in range(0,26):
		ans=0.0
		for j in range(0,length):
			t=ord(x[j])+i
			if t>90:
				t=t-26
			temp=chr(t)
			if temp not in dict:
				dict[temp]=0
			ans=ans+alphebat[temp]*dict[temp]
		M.append(ans/length)
	for i in M:
		temp=abs(i-0.065)
		if temp<min:
			min=temp
			step=M.index(i)
	print ("M is "+str(M[step])+" at "+str(step))'''
	#print(dict)
	'''ans=0.0
	for key,values in dict.items():
		ans=ans+values*(values-1)
	ans=ans/(length*(length-1))
	print (ans)'''
	

'''for m in range(2,8):
	print("the count of strings is "+str(m)+":")
	for j in range(0,m):
		y=[]
		k=j
		while(k<len(text)):
			y.append(text[k])
			k=k+m
		calculate(y)'''
#m=6
'''for j in range(0,6):
	y=[]
	k=j
	while(k<len(text)):
		y.append(text[k])
		k=k+6
	print("calculate string "+''.join(y))
	calculate(y)'''
'''for i in range(0,6):
	y=[]
	j=i
	while(j<len(text)):
		y.append(text[j])
		#print (text[j],j)
		j=j+6
	print("calculate string : "+''.join(y))
	calculate(y)'''

key=[19,7,4,14,17,24]
ans=""
for i in range(0,len(text)):
	temp=ord(text[i])-key[i%6]
	if temp<65:
		temp=temp+26
	ans=ans+chr(temp)
print (ans)