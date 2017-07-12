import re
import sys
error = []
l = ['$','#','@']
password = raw_input("Enter your password ")
if len(password)<6:
	print "Password is too short!"
elif len(password)>16:
	print "password is too long!"
elif not any(x.isupper() for x in password):
    error.append('Your password needs at least 1 capital.')
    if len(error)> 0:
       print error[0]
elif not any(x.islower() for x in password):
    error.append('Your password needs at least 1 small.')
    if len(error) > 0:
       print error[0]
elif not any(x.isdigit() for x in password):
    error.append('Your password needs at least 1 digit')
    if len(error) > 0:
       print error[0]
elif not any(x in password for x in l):
	print "Special characters are required"
else:
	print "Password is fine"

