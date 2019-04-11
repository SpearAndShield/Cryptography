text="EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCKQPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCGOIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUGFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNSACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNCIACZEJNCSHFZEJZEGMXCYHCJUMGKUCY"
dict={}
#signal letter,max locates at "C"
'''for i in text:
	if i in dict:
		dict[i]=dict[i]+1
	else:
		dict[i]=1
for key,values in dict.items():
	print(key,values)
print (dict)'''

#two letters as"C*",max locates at"CG"
length=len(text)
'''for i in range(0,length-1):
	if text[i]=="C":
		if text[i+1] in dict:
			dict[text[i+1]]=dict[text[i+1]]+1
		else:
			dict[text[i+1]]=1'''
#two letters as"*C",max locates as "ZC"
'''for i in range(1,length):
	if text[i]=="C":
		if text[i-1] in dict:
			dict[text[i-1]]=dict[text[i-1]]+1
		else:
			dict[text[i-1]]=1'''
for i in range(0,length-1):
	temp=text[i]+text[i+1]
	if temp in dict:
		dict[temp]=dict[temp]+1
	else:
		dict[temp]=1
max=0
ans="?"
for key,values in dict.items():
	if max<values:
		max=values
		ans=key
	elif max==values:
		ans=ans+" "+key
print(ans,max)
print (dict)