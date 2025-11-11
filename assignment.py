#creatung a string using single quotes, Double quotes and triple Quotes
word1='Hello'
word2=" Welcome"
word3=""" to python Class"""
print(f"{word1}{word2}{word3}")
#create a variable called sentence and assign this text:
sentence= "Python is fun to learn"
print(sentence)
#using a Multiline string to store this short message
multiline_string = """ 
 Python is powerful.
 It is easy to learn.
 It is loved by developers.
 """
print(multiline_string)

#String as Arrays
#create a variable text
text= ("PYTHON")
print(text[0]) 
print(text[3])
print(text[5])

#creating a loop
language="Python"
for letter in language:
    print(letter)

#string length & checking
#creating a varaible fruit
fruits="Banana"
print(len(fruits))   

#creating a variable with if
word = "Learning Python is cool"
if "python" in word:
    print("yes, 'python is found.' ")
if "java" in word:
    print("yes, Java is found.")
else:
    print("no, Java is not found.")

#Bonus Task

message = "Coding is Fun"
count = 0
for letter in message:
     if letter == "n":
        count += 1
print(count)


poem= """ 
I like Python for the way
Its code just seems to flow;
No tangled knots, no endless lines—
Just clean and neat, you know?
 """
print(poem)

#Assignment 2
#Variable and String
#three variable
name="Ada"
age="18"
school = "Bright Future Academy"
print(f"My name is {name}, i am {age} years old, and i attend {school}.")

#Two Variable
country = "Nigeria"
capital = "Abuja"
print(f"The capital of {country} is {capital}.")

#creating three variables
first_name = "John"
middle_name = "Paul"
last_name = "Okoro"
print(f"{ first_name} {middle_name} { last_name}")

#creatiing two variables food
food = "Rice"
drink = "Juice"
print(f"i love eating {food} and {drink}")


