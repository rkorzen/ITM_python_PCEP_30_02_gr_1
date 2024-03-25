
a = 1

def foo():
    b = 10
    
    def bar():
        # global a
        # nonlocal b
        a = 2
        b = 12
        print("a w bar:", a)
        print("b w bar", b)

    bar()
    print("b w foo", b)
  

foo()
print(a)
