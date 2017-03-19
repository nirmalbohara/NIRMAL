print('enter your date of birth in format yyyy-mm-dd')
#year = input('year: ')
#month = input ('month: ')
#day = input ('day: ')
#img = (2017) + (int(month)/365) + (int(day)/365)
#vir = int(year) + (int(month)/365) + (int(day)/365)
#age =  img - vir

#b = input("current year: ")
#d = input('current month: ')
#e = d/12
#c = a.split('-')[0]
#age = int(b)-int(c)
#month = a.split('-')[1]/12
#m = e - month
#print ("your age is : {} and month is: {}" .format(age,int(m)))

dob = input("enter your dob: ")
date_parts = dob.split('-')
[year, month , day] = date_parts

dob_timestamp = float(year) + float(month)/12 + float(day)/365

[today_year, today_month, today_day] = ['2017', '03', '18']
today_timestamp = float(today_year) + float(today_month)/12 + float(today_day)/365

years = today_timestamp - dob_timestamp
months = (years - int(years))* 12
print("your age is %d years %d months" %(years, months))
Chat Conversation End
Type a message...