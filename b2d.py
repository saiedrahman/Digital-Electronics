#inport a number and  make it a string 
print ('Input a binary number (Your number should contain only 0 and 1):')
num= input()
# turn  this number in to string.

x=str(num)
#find the possition of  binary point give it a name d
 
d=x.find('.')
if d==-1:
	d=len(x)
w=0
#if the number is not whole number 
for i in range(d):
	p= d-1-i
	k=int(x[i])* 2**p
	w=k+w


# now trasformation of the later part (lets call it not whole number). which starts from point d+1
b=len(x[d+1:])
i=1
r=0
for i in range (1,b+1):
		k=int(x[d+i])*2**(-i)
		r=k+r	
#return r
dcm=w+r
#Putting this not whole part after decimal point 



print('in decimal the number is: ' +str(dcm))



