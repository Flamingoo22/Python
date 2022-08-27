
# Basic - Print all integers from 0 to 150.
for x in range(151):
    print(x)
    
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,151,5):
    print(x)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,101):
    if not x % 10:
        print("Coding Dojo")
    elif not x % 5:
        print("Dojo")
    else:
        print(x)
        
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
i = 0
for x in range(1,500000,2):
    i += x

print(i)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,1,-4):
    print(i)
    
lowNum = 2
highNum = 312
mult = 12
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
for x in range(lowNum, highNum):
    if not x % mult:
        print(x)