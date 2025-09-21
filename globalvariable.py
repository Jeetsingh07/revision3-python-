
    # print(a)+display()
a = "hello"   # global variable

def display():
    print("inside the function:", a)   # function reads global 'a'

display()
print("outside the function:", a)


#local variable
def display():
    print("hello world hello india")
display()


#modify global variable  to change the variable
a="helllo"
def display():
    global a
    a="world"
    print("hello it is inside the function ",a)
display()
print("hellolll",a)    