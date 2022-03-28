
print("Please Enter your name :?")
name=input()
print("Please Enter your Age :?")
age=input()
print('What\'s your city :?')
city=input()
print("What is your favourite dish :?")
dish=input()
string="Your name is {} . You are {} years old . You live in {}.And your favourite dish is"
output=string.format(name,age,city ,dish)
print(output)
