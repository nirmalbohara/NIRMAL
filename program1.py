names=['john doe','jane doe','johnny turk']
#Change the first name in the list
names[0]='foo bar'
print('names now:', names)
#Append some more names
names.append('molly mormon')
names.append('joe bloggs')
print('names finally:',names)
print('last name in the list: %s' % names[-1])
#You can join lists using str.join() method
joined_names='\n'.join(names)
print('\nlist of names:')
print(joined_names)