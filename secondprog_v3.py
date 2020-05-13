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

print("\n")
print("Hi")
print("your Name is ",name)
print("your age is",age)
print("you've studied ",edu)
print("your marks in math is ",math," in telugu is ",telugu,"your science marks",sci)
print("your subjects total is ",total)
print('\n')
print("Thank you")

