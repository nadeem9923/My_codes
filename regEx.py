import re

def validate_email(email):
print("Please enter email Address: ")
  eMAIL = input()
  email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

  if ( re.fullmatch(email_pattern, email) ):
 print("Email is Valid")
  else:
    print("Email is Invalid")
	
def validate_password(password):	
	print("Please enter password should be \n1) One Capital Letter\n2) Special Character\n3) One Number \n4) Length Should be 8-18: ")
pswd = input()

reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

match_re = re.compile(reg)
res = re.search(match_re, pswd)
if res:
  print("Valid Password")
else:
  print("Invalid Password")