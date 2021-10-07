l = 10 # Global

def function1(n):
    # l = 5 #Local
    m = 8 #Local
    global l  # to change the value of global variable, we have to use global keyword
    l = l + 45  
    print(l, m)
    print(n, "I have printed")

function1("This is me")
# print(m)

x = 89
def harry():
    x = 20
    def rohan():
        global x
        # here it will search for x outside ALL functions, if not exists, then it will create one
        x = 50
    print("before calling rohan() :", x)
    rohan()
    print("after calling rohan() :", x)

harry()
print(x)





  
