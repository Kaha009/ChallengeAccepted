#v1 = 30

#d1,d2 = 0,-90
ct=float(3)
v1,v2 = float(raw_input('Speed of Train 1(Slow Train): ')),float(raw_input('Speed of Train 2(Fast Train):'))#30,60
cv = v1 - v2
cd = v2 * ct
C = abs(float(cd/cv))
A = C - ct
print (A)
#print(d)
"""
t=0
while(d1 > d2):
	t=t+1
	d1=d1+v1
	d2=d2+v2
	print(d1)
	print(d2)
time=str(t)
print('The train with catch up with the first second one in '+time+' hours')
"""