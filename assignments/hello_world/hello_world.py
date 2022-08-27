# # 1. TASK: print "Hello World"
# print("Hello World")
# # 2. print "Hello Noelle!" with the name in a variable
# name = "Yifan"
# print( "Hello", name )	# with a comma
# print( "Hello" + name )	# with a +
# # 3. print "Hello 42!" with the number in a variable
# name = 42
# print( "Hello", name,"!" )	# with a comma
# print( "Hello " + str(name) +"!" )	# with a +	-- this one should give us an error!
# # 4. print "I love to eat sushi and pizza." with the foods in variables
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print( "I love to eat {} and {}.".format(fave_food1,fave_food2)) # with .format()
# print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

#Try out Different string methods

#rearrange a string;
a = "Yifan"
b = a.upper()
print(b)
c = a.lower()
print(c)
d = a.count("i")
print(d)
e = a.split("if")
print(e)
f = a.find("n")
print(f)
g = a.isalnum()
print(g)
i = list(a)
print(i)
h = "3".join(a)
print(h)