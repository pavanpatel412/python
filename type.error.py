try:
    def add(a,b):
       result = a*b
       print(result)
    add(4)
except TypeError:
    print("type error: missing one required positional argument;")
    def add(a,b):
       result = a*b
       print(result)
    add(4,8)
