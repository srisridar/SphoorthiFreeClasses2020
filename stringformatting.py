# that collects name,age,education,3 subject marks ,calculates the total
# and converts all into uppercase and displays the info on the screen
#
#



# collects name,age,education,3 subject marks
name=input("Enter your Name ")
age=input("Enter your age ")
edu=input("Enter your education ")
math=input("Enter your math marks ")
telugu=input("Enter your telugu marks ")
sci=input("Enter your science marks ")

# converts all into uppercase

name=name.upper()
edu=edu.upper()

# calculates the total of 3 subject marks
math=int(math)
sci=int(sci)
telugu=int(telugu)
total= math+sci+telugu

# displays the info on the screen

print(
    """
Hi,
Your name : %s
Your Age : %s
you've studied : %s
your total is : %s """%(name,age,edu,total))


