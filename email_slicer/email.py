
print("Please Enter your email:?")
email=input()
loc=email.find("@")
username=email[:loc]
domain_name=email[loc+1:]
print("Your Username is {} and domain name is {} .".format(username,domain_name))
