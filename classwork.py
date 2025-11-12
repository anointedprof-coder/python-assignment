txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "Hello, and Welcome to My World."
x = txt.casefold()
print (x)

txt = "hello, and welcome to my world."
x = txt.center(50)
print (x)

txt = "john visited john at Mr john's house."
x = txt.count("john")
print (x)

# creatind Encode
txt = "My friend's name is  Ståle"
x = txt.encode()
print(x)
#endswith
txt = "welcome to Africa."
x = txt.endswith(",")
print(x)

#Expendtabs
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

#Find
txt = "Python class is the best class to be."
x=txt.find('is')
print(x)

#format
txt = "For only {price:.2f} dollars!"
b=(txt.format(price = 49))
print(b)

#index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#isalnum (display true if its alphanumeric)
txt = "####"
x = txt.isalnum()
print(x)

#Isalpha (display true if all the characters are alphabet)
txt = "Company2"
x = txt.isalpha()
print(x)

#Isascii  (display true if all the characters are strings)
txt = "####"
x = txt.isascii()
print(x)

#isdecimal()	Returns True if all characters in the string are decimals (0-9)
boy= "8.7"
x = boy.isdecimal()
print(x)

#isdigit()	Returns True if all characters in the string are digits
boy= "ABC"
x = boy.isdigit()
print(x)

#isidentifier()	Returns True if the string is an identifier
boy= "Alpha_numeric"
x = boy.isidentifier()
print(x)