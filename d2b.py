#inport a number and  make it a string 
import math

print ('Input a  number :')
x= input()

#find the possition of  binary point give it a name d
 
d=x.find('.')


if d == -1:
	x=x+'.0'
d=x.find('.')
num=int(x[:d])
w = ''
while(num):
	k = num % 2
	w = str(k) + w
	num = num // 2
m=str(w)

a=int(x[d+1:])

b=len(x[d+1:])
frac=a/(10**b)


f=''
while(frac!=0):
	p=frac*2
		
	k=p//1

	f=str(math.floor(k))+f
	frac=p%1
		
n=str(f)
l=n[::-1]
d='.'

binary=m+d+l
print('In Binary the number is ', binary)
	
	
		
		
	
