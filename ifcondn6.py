x= int(input('coordinate value of x ='))
y=int(input('coordinate value of y ='))
if x==0 and y==0:
	print("its lie on origin.")
elif x>0 and y<0:
	print('its lie on 4th quadrent')	
elif x<0 and y>0:
	print('its lie on 2th quadrent')	
elif x<0 and y<0:
	print('its lie on 1st quadrent')