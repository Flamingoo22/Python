num1 = 42  #variable declaration, number integer
num2 = 2.3  #variable declaration, number float
boolean = True  #variable declaration, boolean
string = 'Hello World'  #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, Composite -List -initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable  declaration, composition - Dictionary - Initialize
fruit = ('blueberry', 'strawberry', 'banana')  #variable declaration, composite -Tuple -initialize
print(type(fruit)) #log statement, type check Output:String
print(pizza_toppings[1])  #log statement, -List -access value   Output:"Sausage"
pizza_toppings.append('Mushrooms')  #-List -add value
print(person['name'])  #log statement, -dictionary -access value   Output: "John"
person['name'] = 'George'   #dictionary -change value   person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person['eye_color'] = 'blue'  #dictionary -add value    person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color':"blue"}
print(fruit[2])   #log statement , tuple -access value    Output:"banana"

if num1 > 45:     #conditional if statement
    print("It's greater")   #log statement    Output: "It's greater"
else:    #conditional else statement
    print("It's lower")    #log statement    

if len(string) < 5:    #condtional if statement
    print("It's a short word!")   #log statement
elif len(string) > 15:      #conditional else if
    print("It's a long word!")      #log statement
else:       #conditional else statement
    print("Just right!")        #log statement      Output: "Just right!"

for x in range(5):      #for loop start     initiate 5 times:1st 0, 2nd 1, 3rd 2, 4th 3, 5th 4, for loop stop
    print(x)        #log statement, for loop stop     Output: x   x   x   x   x  #execute action 5 times
for x in range(2,5):    #for loop start     initiate 3 times: 1st 2, 2nd 3, 3rd 4, for loop stop
    print(x)    #log statement      Output: x   x   x   #execute action 3 times
for x in range(2,10,3):     #for loop start     initiate 3 times:1st 2, 2nd 5, 3rd 8, for loop stop
    print(x)    #log statement   Output: x   x   x   #execute action 3 times
x = 0   #variable declaration, number integer
while(x < 5):   #while loop start   initiate 5 times: 1st 0, 2nd 1, 3rd 2, 4th 3, 5th 4, while loop stop
    print(x)    #log statement  Output: x   x   x   x   x
    x += 1      #while loop increment  1st x=1, 2nd x=2, 3rd x=3, 4th x=4, 5th x=5

pizza_toppings.pop()    #composite -list -delete last value   pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese']
pizza_toppings.pop(1)   #composite -list -delete second value   pizza_toppings = ['Pepperoni',  'Jalepenos', 'Cheese']

print(person)   #log statement, composite -dictionary   Output:person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color':"blue"}
person.pop('eye_color')     #composite -dictionary -delete value    person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
print(person)   #log statement, composite -dictionary   Output: person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:  #for loop start, loop through each element 
    if topping == 'Pepperoni':  #conditional if statement
        continue    # for loop continue :skip pepperoni
    print('After 1st if statement') #log statement Output:execute 3 times
    if topping == 'Olives':     #conditional if statement
        break       #for loop break
#This for loop will print out "After 1st if statement" 3 times, skips once when topping == "pepperoni", and breaks when topping == "Olive"
def print_hello_ten_times():    
    for num in range(10):
        print('Hello')
#function has no argumentm for loop will execute 10 time from 0-9
print_hello_ten_times()
#function is called, will log "Hello" 10 times
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#function has argument x, for loop will execute x numbers of time.
print_hello_x_times(4)
#function is called with argument 4, will log "Hello" 4 times
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#function has default argument/parameter = 10, will execute 10 times if no argument when called.
print_hello_x_or_ten_times()    
#function is called with no argument, will log "Hello" 10 times (default).
print_hello_x_or_ten_times(4)
#function is called, will log "Hello" 4 times.

"""
Bonus section
"""

print(num3) 
#Name Error: num3 is not defined
num3 = 72
#variable declaration  number integer
fruit[0] = 'cranberry'
#- TypeError: 'tuple' object does not support item assignment
print(person['favorite_team'])
#- KeyError: 'favorite_team'
print(pizza_toppings[7])
#- IndexError: list index out of range
print(boolean)
#log statement  Output: True
fruit.append('raspberry')
#- AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1)
#- AttributeError: 'tuple' object has no attribute 'pop'