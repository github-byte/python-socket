import re

hand=open("actual.txt")
count=0

for line in hand:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    if len(x)==0: continue
    for i in range(0,len(x)):
        count+=(int)(x[i])
print(count)   











































































# x="Writing programs (or programming) is ajbbbb@very creative and rewarding activity.  You can write programs for 3036 many reasons, ranging from making your living to solving 7209"
# y=re.findall('[0-9]+',x)                #any numbers
# z=re.findall('[AEIOU]+',x)          #uppercaseVowels
# r=re.findall('[a-z]+',x)            #lowercase
# r2=re.findall('[A-Z]+',x)      #uppercase
# print(y)
# print(z) 
# print(r) 
# print(r2)               #no uppercase vowels
# string=re.findall('^W.+?y',x)
# non_blank=re.findall('^Writing(\S+@ \S+)',x)

# blank=re.findall('\s+Y\s+',x)
# print("Non_blank",non_blank) 
# print('Blank:',blank)                                   #.->anycharacter 
                                                        #+-->one or more times

