# Created by Amin Zeina
# Created on Mar 2018

day = input('Enter the day of the week: ')
age = int(input('Enter your age: '))

if (day == 'Tuesday' or day == 'Thursday') or (age > 12 and age < 21):
	print('You pay student price!')
else:
	print('You pay regular price')

input('Program end.')